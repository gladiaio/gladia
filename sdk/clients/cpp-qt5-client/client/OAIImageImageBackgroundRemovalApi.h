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

#ifndef OAI_OAIImageImageBackgroundRemovalApi_H
#define OAI_OAIImageImageBackgroundRemovalApi_H

#include "OAIHttpRequest.h"

#include "OAIHTTPValidationError.h"
#include "OAIHttpRequest.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>

namespace OpenAPI {

class OAIImageImageBackgroundRemovalApi: public QObject {
    Q_OBJECT

public:
    OAIImageImageBackgroundRemovalApi();
    OAIImageImageBackgroundRemovalApi(QString host, QString basePath);
    ~OAIImageImageBackgroundRemovalApi();

    QString host;
    QString basePath;
    QMap<QString, QString> defaultHeaders;

    void applyImageImageBackgroundRemovalPost(const OAIHttpRequestInputFileElement*& image, const QString& model);
    void getVersionsImageImageBackgroundRemovalGet();
    
private:
    void applyImageImageBackgroundRemovalPostCallback (OAIHttpRequestWorker * worker);
    void getVersionsImageImageBackgroundRemovalGetCallback (OAIHttpRequestWorker * worker);
    
signals:
    void applyImageImageBackgroundRemovalPostSignal(OAIObject summary);
    void getVersionsImageImageBackgroundRemovalGetSignal(OAIObject summary);
    
    void applyImageImageBackgroundRemovalPostSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    void getVersionsImageImageBackgroundRemovalGetSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    
    void applyImageImageBackgroundRemovalPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsImageImageBackgroundRemovalGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    
    void applyImageImageBackgroundRemovalPostSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsImageImageBackgroundRemovalGetSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    
};

}
#endif