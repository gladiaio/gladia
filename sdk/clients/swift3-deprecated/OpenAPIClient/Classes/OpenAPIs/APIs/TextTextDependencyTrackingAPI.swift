//
// TextTextDependencyTrackingAPI.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation
import Alamofire


open class TextTextDependencyTrackingAPI: APIBase {
    /**
     Apply model for the dependency-tracking task for a given models
     - parameter inputString: (query)  (optional)
     - parameter model: (query)  (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func applyTextTextDependencyTrackingPost(inputString: String? = nil, model: String? = nil, completion: @escaping ((_ data: Any?, _ error: ErrorResponse?) -> Void)) {
        applyTextTextDependencyTrackingPostWithRequestBuilder(inputString: inputString, model: model).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Apply model for the dependency-tracking task for a given models
     - POST /text/text/dependency-tracking/
     - parameter inputString: (query)  (optional)
     - parameter model: (query)  (optional)
     - returns: RequestBuilder<Any> 
     */
    open class func applyTextTextDependencyTrackingPostWithRequestBuilder(inputString: String? = nil, model: String? = nil) -> RequestBuilder<Any> {
        let path = "/text/text/dependency-tracking/"
        let URLString = OpenAPIClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems(values:[
            "input_string": inputString,
            "model": model
        ])

        let requestBuilder: RequestBuilder<Any>.Type = OpenAPIClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }

    /**
     Get list of models available for dependency-tracking
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getVersionsTextTextDependencyTrackingGet(completion: @escaping ((_ data: Any?, _ error: ErrorResponse?) -> Void)) {
        getVersionsTextTextDependencyTrackingGetWithRequestBuilder().execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Get list of models available for dependency-tracking
     - GET /text/text/dependency-tracking/
     - returns: RequestBuilder<Any> 
     */
    open class func getVersionsTextTextDependencyTrackingGetWithRequestBuilder() -> RequestBuilder<Any> {
        let path = "/text/text/dependency-tracking/"
        let URLString = OpenAPIClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        
        let url = URLComponents(string: URLString)

        let requestBuilder: RequestBuilder<Any>.Type = OpenAPIClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }

}