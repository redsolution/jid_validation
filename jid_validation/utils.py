from .jid import JID, prep_localpart, prep_host


def _validate_jid(value):
    try:
        return JID(value)
    except:
        return None


def validate_full_jid(value):
    jid = _validate_jid(value)
    if jid and jid.user and jid.host:
        return jid.full()
    else:
        return None


def validate_bare_jid(value):
    jid = _validate_jid(value)
    if jid and jid.user and jid.host:
        return jid.userhost()
    else:
        return None


def validate_server_jid(value):
    jid = _validate_jid(value)
    if jid and jid.host:
        return jid.host
    else:
        return None


def validate_jid(value):
    try:
        jid_obj = JID(value)
    except Exception as e:
        return {'success': False, 'error_message': e}

    if jid_obj.user and jid_obj.host:
        try:
            full_jid = jid_obj.full()
            return {"success": True, "full_jid": full_jid}
        except:
            pass

    return {'success': False, 'error_message': 'Invalid JID.'}


def validate_localpart(value):
    try:
        localpart = prep_localpart(value)
        return {"success": True, "localpart": localpart}
    except Exception as e:
        return {'success': False, 'error_message': e}


def validate_host(value):
    try:
        host = prep_host(value)
        return {"success": True, "host": host}
    except Exception as e:
        return {'success': False, 'error_message': e}
