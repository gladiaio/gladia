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

public class OASTextTextBooleanQuestionGenerationApi {
    OASClient client;

    public OASTextTextBooleanQuestionGenerationApi(OASClient client) {
        this.client = client;
    }

    public OASTextTextBooleanQuestionGenerationApi() {
        this.client = new OASClient();
    }

    public OASClient getClient() {
        return this.client;
    }

    /**
     * Apply model for the boolean-question-generation task for a given models
     * 
     * @param text  (optional, default to 'I lSachin Ramesh Tendulkar is a former international cricketer from India and a former captain of the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket. He is the highest run scorer of all time in International cricket.')
     * @param model  (optional, default to questgen)
     * @return Object
     * @throws OAS.ApiException if fails to make API call
     */
    public Object applyTextTextBooleanQuestionGenerationPost(Map<String, Object> params) {
        List<OAS.Param> query = new List<OAS.Param>();

        // cast query params to verify their expected type
        query.addAll(client.makeParam('text', (String) params.get('text')));
        query.addAll(client.makeParam('model', (String) params.get('model')));

        List<OAS.Param> form = new List<OAS.Param>();

        return (Object) client.invoke(
            'POST', '/text/text/boolean-question-generation/', '',
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
     * Get list of models available for boolean-question-generation
     * 
     * @return Object
     * @throws OAS.ApiException if fails to make API call
     */
    public Object getVersionsTextTextBooleanQuestionGenerationGet() {
        List<OAS.Param> query = new List<OAS.Param>();
        List<OAS.Param> form = new List<OAS.Param>();

        return (Object) client.invoke(
            'GET', '/text/text/boolean-question-generation/', '',
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