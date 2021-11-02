//
// TextTextHateSpeechDetectionAPI.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation
import Alamofire


open class TextTextHateSpeechDetectionAPI: APIBase {
    /**
     Apply model for the hate-speech-detection task for a given models
     - parameter text: (query)  (optional)
     - parameter model: (query)  (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func applyTextTextHateSpeechDetectionPost(text: String? = nil, model: String? = nil, completion: @escaping ((_ data: Any?, _ error: ErrorResponse?) -> Void)) {
        applyTextTextHateSpeechDetectionPostWithRequestBuilder(text: text, model: model).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Apply model for the hate-speech-detection task for a given models
     - POST /text/text/hate-speech-detection/
     - parameter text: (query)  (optional)
     - parameter model: (query)  (optional)
     - returns: RequestBuilder<Any> 
     */
    open class func applyTextTextHateSpeechDetectionPostWithRequestBuilder(text: String? = nil, model: String? = nil) -> RequestBuilder<Any> {
        let path = "/text/text/hate-speech-detection/"
        let URLString = OpenAPIClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems(values:[
            "text": text,
            "model": model
        ])

        let requestBuilder: RequestBuilder<Any>.Type = OpenAPIClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }

    /**
     Get list of models available for hate-speech-detection
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getVersionsTextTextHateSpeechDetectionGet(completion: @escaping ((_ data: Any?, _ error: ErrorResponse?) -> Void)) {
        getVersionsTextTextHateSpeechDetectionGetWithRequestBuilder().execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Get list of models available for hate-speech-detection
     - GET /text/text/hate-speech-detection/
     - returns: RequestBuilder<Any> 
     */
    open class func getVersionsTextTextHateSpeechDetectionGetWithRequestBuilder() -> RequestBuilder<Any> {
        let path = "/text/text/hate-speech-detection/"
        let URLString = OpenAPIClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        
        let url = URLComponents(string: URLString)

        let requestBuilder: RequestBuilder<Any>.Type = OpenAPIClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }

}