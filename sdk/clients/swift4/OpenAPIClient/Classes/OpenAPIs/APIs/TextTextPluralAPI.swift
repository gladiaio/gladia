//
// TextTextPluralAPI.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation
import Alamofire



open class TextTextPluralAPI {
    /**
     * enum for parameter model
     */
    public enum Model_applyTextTextPluralPost: String {
        case inflect = "inflect"
    }

    /**
     Apply model for the plural task for a given models
     
     - parameter word: (query)  (optional, default to "cat")
     - parameter count: (query)  (optional, default to 2)
     - parameter model: (query)  (optional, default to .inflect)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func applyTextTextPluralPost(word: String? = nil, count: Int? = nil, model: Model_applyTextTextPluralPost? = nil, completion: @escaping ((_ data: Any?,_ error: Error?) -> Void)) {
        applyTextTextPluralPostWithRequestBuilder(word: word, count: count, model: model).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }

    /**
     Apply model for the plural task for a given models
     - POST /text/text/plural/
     - parameter word: (query)  (optional, default to "cat")
     - parameter count: (query)  (optional, default to 2)
     - parameter model: (query)  (optional, default to .inflect)
     - returns: RequestBuilder<Any> 
     */
    open class func applyTextTextPluralPostWithRequestBuilder(word: String? = nil, count: Int? = nil, model: Model_applyTextTextPluralPost? = nil) -> RequestBuilder<Any> {
        let path = "/text/text/plural/"
        let URLString = OpenAPIClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
            "word": word, 
            "count": count?.encodeToJSON(), 
            "model": model?.rawValue
        ])

        let requestBuilder: RequestBuilder<Any>.Type = OpenAPIClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }

    /**
     Get list of models available for plural
     
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getVersionsTextTextPluralGet(completion: @escaping ((_ data: Any?,_ error: Error?) -> Void)) {
        getVersionsTextTextPluralGetWithRequestBuilder().execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }

    /**
     Get list of models available for plural
     - GET /text/text/plural/
     - returns: RequestBuilder<Any> 
     */
    open class func getVersionsTextTextPluralGetWithRequestBuilder() -> RequestBuilder<Any> {
        let path = "/text/text/plural/"
        let URLString = OpenAPIClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        
        let url = URLComponents(string: URLString)

        let requestBuilder: RequestBuilder<Any>.Type = OpenAPIClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }

}