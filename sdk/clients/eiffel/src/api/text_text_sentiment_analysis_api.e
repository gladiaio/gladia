note
 description:"[
		FastAPI
 		No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
  		The version of the OpenAPI document: 0.1.0
 	    

  	NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

 		 Do not edit the class manually.
 	]"
	date: "$Date$"
	revision: "$Revision$"
	EIS:"Eiffel openapi generator", "src=https://openapi-generator.tech", "protocol=uri"

class
	TEXTTEXTSENTIMENTANALYSIS_API

inherit

    API_I


feature -- API Access


	apply_text_text_sentiment_analysis_post (text: STRING_32; model: STRING_32): detachable ANY
			-- Apply model for the sentiment-analysis task for a given models
			-- 
			-- 
			-- argument: text  (optional, default to I like you. I love you)
			-- 
			-- argument: model  (optional, default to distilbert-base-uncased-finetuned-sst-2-english)
			-- 
			-- 
			-- Result ANY
		require
		local
  			l_path: STRING
  			l_request: API_CLIENT_REQUEST
  			l_response: API_CLIENT_RESPONSE
		do
			reset_error
			create l_request
			
			l_path := "/text/text/sentiment-analysis/"
			l_request.fill_query_params(api_client.parameter_to_tuple("", "text", text));
			l_request.fill_query_params(api_client.parameter_to_tuple("", "model", model));


			if attached {STRING} api_client.select_header_accept (<<"application/json">>)  as l_accept then
				l_request.add_header(l_accept,"Accept");
			end
			l_request.add_header(api_client.select_header_content_type (<<>>),"Content-Type")
			l_request.set_auth_names (<<>>)
			l_response := api_client.call_api (l_path, "Post", l_request, Void, agent deserializer)
			if l_response.has_error then
				last_error := l_response.error
			elseif attached { ANY } l_response.data ({ ANY }) as l_data then
				Result := l_data
			else
				create last_error.make ("Unknown error: Status response [ " + l_response.status.out + "]")
			end
		end	

	versions_text_text_sentiment_analysis_get : detachable ANY
			-- Get list of models available for sentiment-analysis
			-- 
			-- 
			-- 
			-- Result ANY
		require
		local
  			l_path: STRING
  			l_request: API_CLIENT_REQUEST
  			l_response: API_CLIENT_RESPONSE
		do
			reset_error
			create l_request
			
			l_path := "/text/text/sentiment-analysis/"


			if attached {STRING} api_client.select_header_accept (<<"application/json">>)  as l_accept then
				l_request.add_header(l_accept,"Accept");
			end
			l_request.add_header(api_client.select_header_content_type (<<>>),"Content-Type")
			l_request.set_auth_names (<<>>)
			l_response := api_client.call_api (l_path, "Get", l_request, Void, agent deserializer)
			if l_response.has_error then
				last_error := l_response.error
			elseif attached { ANY } l_response.data ({ ANY }) as l_data then
				Result := l_data
			else
				create last_error.make ("Unknown error: Status response [ " + l_response.status.out + "]")
			end
		end	


end