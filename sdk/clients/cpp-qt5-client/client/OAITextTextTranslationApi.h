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

#ifndef OAI_OAITextTextTranslationApi_H
#define OAI_OAITextTextTranslationApi_H

#include "OAIHttpRequest.h"

#include "OAIHTTPValidationError.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>

namespace OpenAPI {

class OAITextTextTranslationApi: public QObject {
    Q_OBJECT

public:
    OAITextTextTranslationApi();
    OAITextTextTranslationApi(QString host, QString basePath);
    ~OAITextTextTranslationApi();

    QString host;
    QString basePath;
    QMap<QString, QString> defaultHeaders;

    void applyTextTextTranslationPost(const QString& input_string, const QString& source_language, const QString& target_language, const QString& model);
    void getVersionsTextTextTranslationGet();
    
private:
    void applyTextTextTranslationPostCallback (OAIHttpRequestWorker * worker);
    void getVersionsTextTextTranslationGetCallback (OAIHttpRequestWorker * worker);
    
signals:
    void applyTextTextTranslationPostSignal(OAIObject summary);
    void getVersionsTextTextTranslationGetSignal(OAIObject summary);
    
    void applyTextTextTranslationPostSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    void getVersionsTextTextTranslationGetSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    
    void applyTextTextTranslationPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextTranslationGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    
    void applyTextTextTranslationPostSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextTranslationGetSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    
};

}
#endif