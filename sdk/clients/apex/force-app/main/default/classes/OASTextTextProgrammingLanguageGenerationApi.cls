/*
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by the OAS code generator program.
 * https://github.com/OAS-api/OAS-codegen.git
 * Do not edit the class manually.
 */

public class OASTextTextProgrammingLanguageGenerationApi {
    OASClient client;

    public OASTextTextProgrammingLanguageGenerationApi(OASClient client) {
        this.client = client;
    }

    public OASTextTextProgrammingLanguageGenerationApi() {
        this.client = new OASClient();
    }

    public OASClient getClient() {
        return this.client;
    }

    /**
     * Apply model for the programming-language-generation task for a given models
     * 
     * @param codeSnippet  (optional, default to 'def is_palendrome(s):')
     * @param model  (optional, default to sentdex-GPyT)
     * @return Object
     * @throws OAS.ApiException if fails to make API call
     */
    public Object applyTextTextProgrammingLanguageGenerationPost(Map<String, Object> params) {
        List<OAS.Param> query = new List<OAS.Param>();

        // cast query params to verify their expected type
        query.addAll(client.makeParam('code_snippet', (String) params.get('codeSnippet')));
        query.addAll(client.makeParam('model', (String) params.get('model')));

        List<OAS.Param> form = new List<OAS.Param>();

        return (Object) client.invoke(
            'POST', '/text/text/programming-language-generation/', '',
            query, form,
            new Map<String, Object>(),
            new Map<String, Object>(),
            new List<String>{ 'application/json' },
            new List<String>(),
            new List<String>(),
            Object.class
        );
    }
    /**
     * Get list of models available for programming-language-generation
     * 
     * @return Object
     * @throws OAS.ApiException if fails to make API call
     */
    public Object getVersionsTextTextProgrammingLanguageGenerationGet() {
        List<OAS.Param> query = new List<OAS.Param>();
        List<OAS.Param> form = new List<OAS.Param>();

        return (Object) client.invoke(
            'GET', '/text/text/programming-language-generation/', '',
            query, form,
            new Map<String, Object>(),
            new Map<String, Object>(),
            new List<String>{ 'application/json' },
            new List<String>(),
            new List<String>(),
            Object.class
        );
    }
}