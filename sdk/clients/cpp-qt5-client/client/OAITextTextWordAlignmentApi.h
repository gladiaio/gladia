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

#ifndef OAI_OAITextTextWordAlignmentApi_H
#define OAI_OAITextTextWordAlignmentApi_H

#include "OAIHttpRequest.h"

#include "OAIHTTPValidationError.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>

namespace OpenAPI {

class OAITextTextWordAlignmentApi: public QObject {
    Q_OBJECT

public:
    OAITextTextWordAlignmentApi();
    OAITextTextWordAlignmentApi(QString host, QString basePath);
    ~OAITextTextWordAlignmentApi();

    QString host;
    QString basePath;
    QMap<QString, QString> defaultHeaders;

    void applyTextTextWordAlignmentPost(const QString& input_string_language_1, const QString& input_string_language_2, const QString& model);
    void getVersionsTextTextWordAlignmentGet();
    
private:
    void applyTextTextWordAlignmentPostCallback (OAIHttpRequestWorker * worker);
    void getVersionsTextTextWordAlignmentGetCallback (OAIHttpRequestWorker * worker);
    
signals:
    void applyTextTextWordAlignmentPostSignal(OAIObject summary);
    void getVersionsTextTextWordAlignmentGetSignal(OAIObject summary);
    
    void applyTextTextWordAlignmentPostSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    void getVersionsTextTextWordAlignmentGetSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    
    void applyTextTextWordAlignmentPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextWordAlignmentGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    
    void applyTextTextWordAlignmentPostSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextWordAlignmentGetSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    
};

}
#endif