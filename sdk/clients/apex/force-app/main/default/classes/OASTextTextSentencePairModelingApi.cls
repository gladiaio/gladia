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

public class OASTextTextSentencePairModelingApi {
    OASClient client;

    public OASTextTextSentencePairModelingApi(OASClient client) {
        this.client = client;
    }

    public OASTextTextSentencePairModelingApi() {
        this.client = new OASClient();
    }

    public OASClient getClient() {
        return this.client;
    }

    /**
     * Apply model for the sentence-pair-modeling task for a given models
     * 
     * @param sentence  (optional, default to 'Once, a group of frogs was roaming around the forest in search of water.')
     * @param model  (optional, default to 'UKPLab-all-MiniLM-L6-v2')
     * @return Object
     * @throws OAS.ApiException if fails to make API call
     */
    public Object applyTextTextSentencePairModelingPost(Map<String, Object> params) {
        List<OAS.Param> query = new List<OAS.Param>();

        // cast query params to verify their expected type
        query.addAll(client.makeParam('sentence', (String) params.get('sentence')));
        query.addAll(client.makeParam('model', (String) params.get('model')));

        List<OAS.Param> form = new List<OAS.Param>();

        return (Object) client.invoke(
            'POST', '/text/text/sentence-pair-modeling/', '',
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
     * Get list of models available for sentence-pair-modeling
     * 
     * @return Object
     * @throws OAS.ApiException if fails to make API call
     */
    public Object getVersionsTextTextSentencePairModelingGet() {
        List<OAS.Param> query = new List<OAS.Param>();
        List<OAS.Param> form = new List<OAS.Param>();

        return (Object) client.invoke(
            'GET', '/text/text/sentence-pair-modeling/', '',
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