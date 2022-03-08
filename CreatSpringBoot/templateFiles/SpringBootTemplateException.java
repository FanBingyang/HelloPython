package com.byfan.springboottemplate.exception;

import com.byfan.springboottemplate.common.CommonResponse;

/**
 * @Author: byfan
 * @Description 服务端抛出异常
 * @Version 1.0
 * @Date: 2021/12/8 21:35
 */
public class SpringBootTemplateException extends Exception{

    private Integer errorCode;

    public SpringBootTemplateException(CommonResponse commonResponse) {
        super(commonResponse.msg);
        this.errorCode = commonResponse.code;
    }

    public SpringBootTemplateException(String message) {
        super(message);
        this.errorCode = CommonResponse.UNKNOWN_ERROR.code;
    }

    public SpringBootTemplateException(CommonResponse commonResponse, String message) {
        super(message);
        this.errorCode = commonResponse.code;
    }


    public Integer getErrorCode() {
        return errorCode;
    }

    public void setErrorCode(Integer errorCode) {
        this.errorCode = errorCode;
    }

}