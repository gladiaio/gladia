#import <Foundation/Foundation.h>
#import "OAIHTTPValidationError.h"
#import "OAIApi.h"

/**
* FastAPI
* No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
*
* The version of the OpenAPI document: 0.1.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/



@interface OAITextTextSimilarityApi: NSObject <OAIApi>

extern NSString* kOAITextTextSimilarityApiErrorDomain;
extern NSInteger kOAITextTextSimilarityApiMissingParamErrorCode;

-(instancetype) initWithApiClient:(OAIApiClient *)apiClient NS_DESIGNATED_INITIALIZER;

/// Apply model for the similarity task for a given models
/// 
///
/// @param sentence1  (optional) (default to @"I like Python because I can build AI applications")
/// @param sentence2  (optional) (default to @"Second sentence to compare to")
/// @param model  (optional) (default to @"all-MiniLM-L6-v2")
/// 
///  code:200 message:"Successful Response",
///  code:422 message:"Validation Error"
///
/// @return NSObject*
-(NSURLSessionTask*) applyTextTextSimilarityPostWithSentence1: (NSString*) sentence1
    sentence2: (NSString*) sentence2
    model: (NSString*) model
    completionHandler: (void (^)(NSObject* output, NSError* error)) handler;


/// Get list of models available for similarity
/// 
///
/// 
///  code:200 message:"Successful Response"
///
/// @return NSObject*
-(NSURLSessionTask*) getVersionsTextTextSimilarityGetWithCompletionHandler: 
    (void (^)(NSObject* output, NSError* error)) handler;



@end