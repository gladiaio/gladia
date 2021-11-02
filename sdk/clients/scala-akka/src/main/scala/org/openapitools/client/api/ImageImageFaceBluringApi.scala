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
package org.openapitools.client.api

import java.io.File
import org.openapitools.client.model.HTTPValidationError
import org.openapitools.client.core._
import org.openapitools.client.core.CollectionFormats._
import org.openapitools.client.core.ApiKeyLocations._

object ImageImageFaceBluringApi {

  def apply(baseUrl: String = "http://localhost") = new ImageImageFaceBluringApi(baseUrl)
}

class ImageImageFaceBluringApi(baseUrl: String) {
  
  /**
   * Expected answers:
   *   code 200 : Any (Successful Response)
   *   code 422 : HTTPValidationError (Validation Error)
   * 
   * @param image 
   * @param model 
   */
  def applyImageImageFaceBluringPost(image: File, model: Option[String] = None): ApiRequest[Any] =
    ApiRequest[Any](ApiMethods.POST, "http://localhost", "/image/image/face-bluring/", "multipart/form-data")
      .withFormParam("image", image)
      .withQueryParam("model", model)
      .withSuccessResponse[Any](200)
      .withErrorResponse[HTTPValidationError](422)
      

  /**
   * Expected answers:
   *   code 200 : Any (Successful Response)
   */
  def getVersionsImageImageFaceBluringGet(): ApiRequest[Any] =
    ApiRequest[Any](ApiMethods.GET, "http://localhost", "/image/image/face-bluring/", "application/json")
      .withSuccessResponse[Any](200)
      



}
