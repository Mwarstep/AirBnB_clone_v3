#!/usr/bin/python3
"""
Will handle Review objects and operations
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.review import Review


@app_views.route("/places/<place_id>/reviews", methods=["GET"],
                 strict_slashes=False)
def reviews_by_place(place_id):
    """
    Will retrieve all Review objects by place
    """
    review_list = []
    place_obj = storage.get("Place", str(place_id))

    if place_obj is None:
        abort(404)

    for obj in place_obj.reviews:
        review_list.append(obj.to_json())

    return jsonify(review_list)


@app_views.route("/places/<place_id>/reviews", methods=["POST"],
                 strict_slashes=False)
def review_create(place_id):
    """
    Will Create Review route
    """
    review_json = request.get_json(silent=True)
    if review_json is None:
        abort(400, 'Not a JSON')
    if not storage.get("Place", place_id):
        abort(404)
    if not storage.get("User", review_json["user_id"]):
        abort(404)
    if "user_id" not in review_json:
        abort(400, 'Missing user_id')
    if "text" not in review_json:
        abort(400, 'Missing text')

    review_json["place_id"] = place_id

    new_review = Review(**review_json)
    new_review.save()
    resp = jsonify(new_review.to_json())
    resp.status_code = 201

    return resp


@app_views.route("/reviews/<review_id>",  methods=["GET"],
                 strict_slashes=False)
def review_by_id(review_id):
    """
    Wil Get a specific Review object by ID
    """

    fetched_obj = storage.get("Review", str(review_id))

    if fetched_obj is None:
        abort(404)

    return jsonify(fetched_obj.to_json())


@app_views.route("/reviews/<review_id>",  methods=["PUT"],
                 strict_slashes=False)
def review_put(review_id):
    """
    Will Update specific Review object by ID
    """
    place_json = request.get_json(silent=True)

    if place_json is None:
        abort(400, 'Not a JSON')

    fetched_obj = storage.get("Review", str(review_id))

    if fetched_obj is None:
        abort(404)

    for key, val in place_json.items():
        if key not in ["id", "created_at", "updated_at", "user_id",
                       "place_id"]:
            setattr(fetched_obj, key, val)

    fetched_obj.save()

    return jsonify(fetched_obj.to_json())


@app_views.route("/reviews/<review_id>",  methods=["DELETE"],
                 strict_slashes=False)
def review_delete_by_id(review_id):
    """
    Will Delete Review by id
    """

    fetched_obj = storage.get("Review", str(review_id))

    if fetched_obj is None:
        abort(404)

    storage.delete(fetched_obj)
    storage.save()

    return jsonify({})
