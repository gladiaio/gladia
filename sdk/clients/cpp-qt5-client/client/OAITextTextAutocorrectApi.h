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

#ifndef OAI_OAITextTextAutocorrectApi_H
#define OAI_OAITextTextAutocorrectApi_H

#include "OAIHttpRequest.h"

#include "OAIHTTPValidationError.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>

namespace OpenAPI {

class OAITextTextAutocorrectApi: public QObject {
    Q_OBJECT

public:
    OAITextTextAutocorrectApi();
    OAITextTextAutocorrectApi(QString host, QString basePath);
    ~OAITextTextAutocorrectApi();

    QString host;
    QString basePath;
    QMap<QString, QString> defaultHeaders;

    void applyTextTextAutocorrectPost(const QString& sentence, const QString& model);
    void getVersionsTextTextAutocorrectGet();
    
private:
    void applyTextTextAutocorrectPostCallback (OAIHttpRequestWorker * worker);
    void getVersionsTextTextAutocorrectGetCallback (OAIHttpRequestWorker * worker);
    
signals:
    void applyTextTextAutocorrectPostSignal(OAIObject summary);
    void getVersionsTextTextAutocorrectGetSignal(OAIObject summary);
    
    void applyTextTextAutocorrectPostSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    void getVersionsTextTextAutocorrectGetSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    
    void applyTextTextAutocorrectPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextAutocorrectGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    
    void applyTextTextAutocorrectPostSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextAutocorrectGetSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    
};

}
#endif