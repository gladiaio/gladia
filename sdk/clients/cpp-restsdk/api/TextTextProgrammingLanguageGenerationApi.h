/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI-Generator 4.0.0.
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * TextTextProgrammingLanguageGenerationApi.h
 *
 * 
 */

#ifndef ORG_OPENAPITOOLS_CLIENT_API_TextTextProgrammingLanguageGenerationApi_H_
#define ORG_OPENAPITOOLS_CLIENT_API_TextTextProgrammingLanguageGenerationApi_H_


#include "../ApiClient.h"

#include "HTTPValidationError.h"
#include "Object.h"
#include <cpprest/details/basic_types.h>


#include <boost/optional.hpp>

namespace org {
namespace openapitools {
namespace client {
namespace api {

using namespace org::openapitools::client::model;



class  TextTextProgrammingLanguageGenerationApi 
{
public:

    explicit TextTextProgrammingLanguageGenerationApi( std::shared_ptr<ApiClient> apiClient );

    virtual ~TextTextProgrammingLanguageGenerationApi();

    /// <summary>
    /// Apply model for the programming-language-generation task for a given models
    /// </summary>
    /// <remarks>
    /// 
    /// </remarks>
    /// <param name="codeSnippet"> (optional, default to utility::conversions::to_string_t(&quot;&quot;))</param>
    /// <param name="model"> (optional, default to utility::conversions::to_string_t(&quot;&quot;))</param>
    pplx::task<std::shared_ptr<Object>> applyTextTextProgrammingLanguageGenerationPost(
        boost::optional<utility::string_t> codeSnippet,
        boost::optional<utility::string_t> model
    );
    /// <summary>
    /// Get list of models available for programming-language-generation
    /// </summary>
    /// <remarks>
    /// 
    /// </remarks>
    pplx::task<std::shared_ptr<Object>> getVersionsTextTextProgrammingLanguageGenerationGet(
    );

protected:
    std::shared_ptr<ApiClient> m_ApiClient;
};

}
}
}
}

#endif /* ORG_OPENAPITOOLS_CLIENT_API_TextTextProgrammingLanguageGenerationApi_H_ */
