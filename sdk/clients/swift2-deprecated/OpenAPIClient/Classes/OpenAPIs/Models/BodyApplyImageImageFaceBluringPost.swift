//
// BodyApplyImageImageFaceBluringPost.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation


public class BodyApplyImageImageFaceBluringPost: JSONEncodable {
    public var image: NSURL?

    public init() {}

    // MARK: JSONEncodable
    func encodeToJSON() -> AnyObject {
        var nillableDictionary = [String:AnyObject?]()
        nillableDictionary["image"] = self.image?.encodeToJSON()
        let dictionary: [String:AnyObject] = APIHelper.rejectNil(nillableDictionary) ?? [:]
        return dictionary
    }
}