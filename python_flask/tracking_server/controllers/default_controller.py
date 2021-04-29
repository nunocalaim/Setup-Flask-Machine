import connexion
import six

from tracking_server.models.alias_body import AliasBody  # noqa: E501
from tracking_server.models.profile_body import ProfileBody  # noqa: E501
from tracking_server.models.track_body import TrackBody  # noqa: E501
from tracking_server import util

import json




def alias_post(body):  # noqa: E501
    """Assotiate different identifiers to the same entity.

    Set up a link between the events registered with different userIds.   For example when a user arrives to your website and you start to log  events, you may want to associate the events with a generated ID  that is associated with a cookie. Then, say the user registers and the email address becomes known which means that we now have the ability to associate the previous browsing events with an email address.  At this point you would issue the request with the &#x60;newUserId&#x60; set to the email address and the &#x60;originalUserId&#x60; set to the originally generated ID. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AliasBody.from_dict(connexion.request.get_json())  # noqa: E501
        with open('post-alias-{}-{}.json'.format(body.new_user_id, body.timestamp_utc), 'w') as file:
            json.dump(connexion.request.get_json(), file)
    return ''


def profile_post(body):  # noqa: E501
    """Save profile attributes for an particular user

    This endpoint allows us to save information related to a particular user that either changes very infrequently or does not change at all. For example, birthday, native language, and home country.  If a profile does not exist for a user, it is created the first time you execute a &#x60;/profile&#x60; call. Subsequent calls will merge the new information with the old information in the case that the keys don&#x27;t exist. In the case where keys already exist, the latest call replaces the old value with the new one. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ProfileBody.from_dict(connexion.request.get_json())  # noqa: E501
        with open('post-profile-{}-{}.json'.format(body.user_id, body.timestamp_utc), 'w') as file:
            json.dump(connexion.request.get_json(), file)
    return ''


def track_post(body):  # noqa: E501
    """Log events related with a particular user

    In order to log an event you will be required to provide an userId and  an eventName. You can add more metadata to the log depending on the kind of event that you are logging. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TrackBody.from_dict(connexion.request.get_json())  # noqa: E501
        with open('post-track-{}-{}.json'.format(body.user_id, body.events[-1].timestamp_utc), 'w') as file:
            json.dump(connexion.request.get_json(), file)
    return ''
