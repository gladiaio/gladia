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

/**
 * OASBodyApplyImageImageRestorationPos
 */
public class OASBodyApplyImageImageRestorationPos {
    /**
     * Get image
     * @return image
     */
    public Blob image { get; set; }

    public static OASBodyApplyImageImageRestorationPos getExample() {
        OASBodyApplyImageImageRestorationPos bodyApplyImageImageRestorationPost = new OASBodyApplyImageImageRestorationPos();
          bodyApplyImageImageRestorationPost.image = EncodingUtil.base64Decode(VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2cu);
        return bodyApplyImageImageRestorationPost;
    }

    public Boolean equals(Object obj) {
        if (obj instanceof OASBodyApplyImageImageRestorationPos) {           
            OASBodyApplyImageImageRestorationPos bodyApplyImageImageRestorationPost = (OASBodyApplyImageImageRestorationPos) obj;
            return this.image == bodyApplyImageImageRestorationPost.image;
        }
        return false;
    }

    public Integer hashCode() {
        Integer hashCode = 43;
        hashCode = (17 * hashCode) + (image == null ? 0 : System.hashCode(image));
        return hashCode;
    }
}
