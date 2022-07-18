package policy.ingress

import input.attributes.request.http as http_request
import input.attributes.request.http.headers.authorization as authorization

request_path_array := split(http_request.path, "/")

# anyone with a valid jwt can request their ip
# allow {
#     http_request.path = "/ip"
# 	http_request.method == "GET"
	
# 	validate_jwt
# }

# only members of the twdps-core-labs-team github team in the ThoughtWorks-DPS org may view headers
# allow {
#     http_request.path = "/headers"
# 	http_request.method == "GET"
# 	has(claims, "ThoughtWorks-DPS/twdps-core-labs-team")
	
# 	validate_jwt
# }

# allow anyone to call the status action with any HTTP method if they have a valid jwt from our auth0 app
# note: I check against the first element inthe request_path_array rather than just referencing
# the normal path input. This is only because httpbin/status/{code} expects a code and will accept
# any. 
allow {
	request_path_array[1] == "status"
	
	# validate_jwt
}


# ========================================= shared functions and variables

# claims := c {
#     [header, payload, signature] := io.jwt.decode(bearer_token)
# 	team_membership_claims_title := "https://github.org/ThoughtWorks-DPS/teams"
# 	c := payload[team_membership_claims_title]
# }

# has(x, elem) {
# 	x[_] = elem
# }

# validate_jwt {
# 	[header, payload, signature] := io.jwt.decode(bearer_token)
	
# 	header.alg == "RS256"
# 	payload.iss == "https://dev-twdpsio.us.auth0.com/"
# 	verify_signature
# }

# verify_signature {
# 	io.jwt.verify_rs256(bearer_token, jwks)
# }

# bearer_token := t {
# 	v := authorization
# 	startswith(v, "Bearer ")
# 	t := substring(v, count("Bearer "), -1)
# }

# jwks_request(url) := http.send({
#     "url": url,
#     "method": "GET",
#     "force_cache": true,
#     "force_cache_duration_seconds": 3600 # Cache response for an hour
# })

# jwks := jwks_request("https://dev-twdpsio.us.auth0.com/.well-known/jwks.json").raw_body

