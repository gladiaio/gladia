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



@interface OAITextTextWordAlignmentApi: NSObject <OAIApi>

extern NSString* kOAITextTextWordAlignmentApiErrorDomain;
extern NSInteger kOAITextTextWordAlignmentApiMissingParamErrorCode;

-(instancetype) initWithApiClient:(OAIApiClient *)apiClient NS_DESIGNATED_INITIALIZER;

/// Apply model for the word-alignment task for a given models
/// 
///
/// @param inputStringLanguage1  (optional) (default to @"Sentence from first language")
/// @param inputStringLanguage2  (optional) (default to @"来自 第一 语言的 句子")
/// @param model  (optional) (default to @"bert-base-multilingual-cased")
/// 
///  code:200 message:"Successful Response",
///  code:422 message:"Validation Error"
///
/// @return NSObject*
-(NSURLSessionTask*) applyTextTextWordAlignmentPostWithInputStringLanguage1: (NSString*) inputStringLanguage1
    inputStringLanguage2: (NSString*) inputStringLanguage2
    model: (NSString*) model
    completionHandler: (void (^)(NSObject* output, NSError* error)) handler;


/// Get list of models available for word-alignment
/// 
///
/// 
///  code:200 message:"Successful Response"
///
/// @return NSObject*
-(NSURLSessionTask*) getVersionsTextTextWordAlignmentGetWithCompletionHandler: 
    (void (^)(NSObject* output, NSError* error)) handler;



@end