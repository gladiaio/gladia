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

#ifndef OAI_OAITextTextKeywordExtractionApi_H
#define OAI_OAITextTextKeywordExtractionApi_H

#include "OAIHttpRequest.h"

#include "OAIHTTPValidationError.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>

namespace OpenAPI {

class OAITextTextKeywordExtractionApi: public QObject {
    Q_OBJECT

public:
    OAITextTextKeywordExtractionApi();
    OAITextTextKeywordExtractionApi(QString host, QString basePath);
    ~OAITextTextKeywordExtractionApi();

    QString host;
    QString basePath;
    QMap<QString, QString> defaultHeaders;

    void applyTextTextKeywordExtractionPost(const QString& text, const QString& model);
    void getVersionsTextTextKeywordExtractionGet();
    
private:
    void applyTextTextKeywordExtractionPostCallback (OAIHttpRequestWorker * worker);
    void getVersionsTextTextKeywordExtractionGetCallback (OAIHttpRequestWorker * worker);
    
signals:
    void applyTextTextKeywordExtractionPostSignal(OAIObject summary);
    void getVersionsTextTextKeywordExtractionGetSignal(OAIObject summary);
    
    void applyTextTextKeywordExtractionPostSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    void getVersionsTextTextKeywordExtractionGetSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    
    void applyTextTextKeywordExtractionPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextKeywordExtractionGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    
    void applyTextTextKeywordExtractionPostSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextKeywordExtractionGetSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    
};

}
#endif