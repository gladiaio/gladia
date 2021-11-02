//
// TextTextAutocorrectAPI.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Alamofire



public class TextTextAutocorrectAPI: APIBase {
    /**
     * enum for parameter model
     */
    public enum Model_applyTextTextAutocorrectPost: String { 
        case FlexudyT5BaseMultiSentenceDoctor = "flexudy-t5-base-multi-sentence-doctor"
    }

    /**
     Apply model for the autocorrect task for a given models
     
     - parameter sentence: (query)  (optional)
     - parameter model: (query)  (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    public class func applyTextTextAutocorrectPost(sentence sentence: String? = nil, model: Model_applyTextTextAutocorrectPost? = nil, completion: ((data: AnyObject?, error: ErrorType?) -> Void)) {
        applyTextTextAutocorrectPostWithRequestBuilder(sentence: sentence, model: model).execute { (response, error) -> Void in
            completion(data: response?.body, error: error);
        }
    }


    /**
     Apply model for the autocorrect task for a given models
     - POST /text/text/autocorrect/     - parameter sentence: (query)  (optional)
     - parameter model: (query)  (optional)

     - returns: RequestBuilder<AnyObject> 
     */
    public class func applyTextTextAutocorrectPostWithRequestBuilder(sentence sentence: String? = nil, model: Model_applyTextTextAutocorrectPost? = nil) -> RequestBuilder<AnyObject> {
        let path = "/text/text/autocorrect/"
        let URLString = OpenAPIClientAPI.basePath + path

        let nillableParameters: [String:AnyObject?] = [
            "sentence": sentence,
            "model": model?.rawValue
        ]
 
        let parameters = APIHelper.rejectNil(nillableParameters)
 
        let convertedParameters = APIHelper.convertBoolToString(parameters)
 
        let requestBuilder: RequestBuilder<AnyObject>.Type = OpenAPIClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "POST", URLString: URLString, parameters: convertedParameters, isBody: false)
    }

    /**
     Get list of models available for autocorrect
     
     - parameter completion: completion handler to receive the data and the error objects
     */
    public class func getVersionsTextTextAutocorrectGet(completion: ((data: AnyObject?, error: ErrorType?) -> Void)) {
        getVersionsTextTextAutocorrectGetWithRequestBuilder().execute { (response, error) -> Void in
            completion(data: response?.body, error: error);
        }
    }


    /**
     Get list of models available for autocorrect
     - GET /text/text/autocorrect/
     - returns: RequestBuilder<AnyObject> 
     */
    public class func getVersionsTextTextAutocorrectGetWithRequestBuilder() -> RequestBuilder<AnyObject> {
        let path = "/text/text/autocorrect/"
        let URLString = OpenAPIClientAPI.basePath + path

        let nillableParameters: [String:AnyObject?] = [:]
 
        let parameters = APIHelper.rejectNil(nillableParameters)
 
        let convertedParameters = APIHelper.convertBoolToString(parameters)
 
        let requestBuilder: RequestBuilder<AnyObject>.Type = OpenAPIClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: URLString, parameters: convertedParameters, isBody: true)
    }

}