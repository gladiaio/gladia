--  FastAPI
--  No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
--
--  The version of the OpenAPI document: 0.1.0
--  
--
--  NOTE: This package is auto generated by OpenAPI-Generator 4.0.0.
--  https://openapi-generator.tech
--  Do not edit the class manually.

with Swagger.Streams;
with Ada.Containers.Vectors;
package .Models is


   --  ------------------------------
   --  ValidationError
   --  ------------------------------
   type ValidationErrorType is
     record
       Loc : Swagger.UString_Vectors.Vector;
       Msg : Swagger.UString;
       P_Type : Swagger.UString;
     end record;

   package ValidationErrorType_Vectors is
      new Ada.Containers.Vectors (Index_Type   => Positive,
                                  Element_Type => ValidationErrorType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in ValidationErrorType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in ValidationErrorType_Vectors.Vector);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out ValidationErrorType);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out ValidationErrorType_Vectors.Vector);



   --  ------------------------------
   --  HTTPValidationError
   --  ------------------------------
   type HTTPValidationErrorType is
     record
       Detail : .Models.ValidationErrorType_Vectors.Vector;
     end record;

   package HTTPValidationErrorType_Vectors is
      new Ada.Containers.Vectors (Index_Type   => Positive,
                                  Element_Type => HTTPValidationErrorType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in HTTPValidationErrorType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in HTTPValidationErrorType_Vectors.Vector);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out HTTPValidationErrorType);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out HTTPValidationErrorType_Vectors.Vector);



   --  ------------------------------
   --  Body_apply_image_image_background_removal__post
   --  ------------------------------
   type BodyApplyImageImageBackgroundRemovalPostType is
     record
       Image : Swagger.Http_Content_Type;
     end record;

   package BodyApplyImageImageBackgroundRemovalPostType_Vectors is
      new Ada.Containers.Vectors (Index_Type   => Positive,
                                  Element_Type => BodyApplyImageImageBackgroundRemovalPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageBackgroundRemovalPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageBackgroundRemovalPostType_Vectors.Vector);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageBackgroundRemovalPostType);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageBackgroundRemovalPostType_Vectors.Vector);



   --  ------------------------------
   --  Body_apply_image_image_colorization__post
   --  ------------------------------
   type BodyApplyImageImageColorizationPostType is
     record
       Image : Swagger.Http_Content_Type;
     end record;

   package BodyApplyImageImageColorizationPostType_Vectors is
      new Ada.Containers.Vectors (Index_Type   => Positive,
                                  Element_Type => BodyApplyImageImageColorizationPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageColorizationPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageColorizationPostType_Vectors.Vector);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageColorizationPostType);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageColorizationPostType_Vectors.Vector);



   --  ------------------------------
   --  Body_apply_image_image_face_bluring__post
   --  ------------------------------
   type BodyApplyImageImageFaceBluringPostType is
     record
       Image : Swagger.Http_Content_Type;
     end record;

   package BodyApplyImageImageFaceBluringPostType_Vectors is
      new Ada.Containers.Vectors (Index_Type   => Positive,
                                  Element_Type => BodyApplyImageImageFaceBluringPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageFaceBluringPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageFaceBluringPostType_Vectors.Vector);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageFaceBluringPostType);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageFaceBluringPostType_Vectors.Vector);



   --  ------------------------------
   --  Body_apply_image_image_restoration__post
   --  ------------------------------
   type BodyApplyImageImageRestorationPostType is
     record
       Image : Swagger.Http_Content_Type;
     end record;

   package BodyApplyImageImageRestorationPostType_Vectors is
      new Ada.Containers.Vectors (Index_Type   => Positive,
                                  Element_Type => BodyApplyImageImageRestorationPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageRestorationPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageRestorationPostType_Vectors.Vector);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageRestorationPostType);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageRestorationPostType_Vectors.Vector);



   --  ------------------------------
   --  Body_apply_image_image_super_resolution__post
   --  ------------------------------
   type BodyApplyImageImageSuperResolutionPostType is
     record
       Image : Swagger.Http_Content_Type;
     end record;

   package BodyApplyImageImageSuperResolutionPostType_Vectors is
      new Ada.Containers.Vectors (Index_Type   => Positive,
                                  Element_Type => BodyApplyImageImageSuperResolutionPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageSuperResolutionPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageSuperResolutionPostType_Vectors.Vector);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageSuperResolutionPostType);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageSuperResolutionPostType_Vectors.Vector);



   --  ------------------------------
   --  Body_apply_image_image_uncolorization__post
   --  ------------------------------
   type BodyApplyImageImageUncolorizationPostType is
     record
       Image : Swagger.Http_Content_Type;
     end record;

   package BodyApplyImageImageUncolorizationPostType_Vectors is
      new Ada.Containers.Vectors (Index_Type   => Positive,
                                  Element_Type => BodyApplyImageImageUncolorizationPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageUncolorizationPostType);

   procedure Serialize (Into  : in out Swagger.Streams.Output_Stream'Class;
                        Name  : in String;
                        Value : in BodyApplyImageImageUncolorizationPostType_Vectors.Vector);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageUncolorizationPostType);

   procedure Deserialize (From  : in Swagger.Value_Type;
                          Name  : in String;
                          Value : out BodyApplyImageImageUncolorizationPostType_Vectors.Vector);



end .Models;