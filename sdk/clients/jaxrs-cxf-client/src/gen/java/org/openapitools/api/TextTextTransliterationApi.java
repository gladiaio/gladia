package org.openapitools.api;

import org.openapitools.model.HTTPValidationError;

import java.io.InputStream;
import java.io.OutputStream;
import java.util.List;
import java.util.Map;
import javax.ws.rs.*;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;
import org.apache.cxf.jaxrs.ext.multipart.*;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import io.swagger.jaxrs.PATCH;

/**
 * FastAPI
 *
 * <p>No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 */
@Path("/")
@Api(value = "/", description = "")
public interface TextTextTransliterationApi  {

    /**
     * Apply model for the transliteration task for a given models
     *
     */
    @POST
    @Path("/text/text/transliteration/")
    @Produces({ "application/json" })
    @ApiOperation(value = "Apply model for the transliteration task for a given models", tags={  })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Successful Response", response = Object.class),
        @ApiResponse(code = 422, message = "Validation Error", response = HTTPValidationError.class) })
    public Object applyTextTextTransliterationPost(@QueryParam("text") @DefaultValue("Лорем ипсум долор сит амет")String text, @QueryParam("language") @DefaultValue("ru")String language, @QueryParam("model") @DefaultValue("transliterate")String model);

    /**
     * Get list of models available for transliteration
     *
     */
    @GET
    @Path("/text/text/transliteration/")
    @Produces({ "application/json" })
    @ApiOperation(value = "Get list of models available for transliteration", tags={  })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Successful Response", response = Object.class) })
    public Object getVersionsTextTextTransliterationGet();
}
