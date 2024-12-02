def viewed_auth(request, user):
  profile = user.profile
  session_viewed = request.session.get('recently_viewed', [])
  profile_viewed = profile.recently_viewed
  combined_viewed = list(dict.fromkeys(profile_viewed + session_viewed))[:10]
  profile.recently_viewed = combined_viewed
  profile.save()
  request.session['recently_viewed'] = combined_viewed
  request.session.modified = True