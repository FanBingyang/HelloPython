package com.byfan.springboottemplate.common;


/**
 * @Author: byfan
 * @Description
 * @Version 1.0
 * @Date: 2021/12/8 21:30
 */
public enum CommonResponse {

    OK(200, "success"),
    UNKNOWN_ERROR(1000, "未知错误"),
    PARAM_ERROR(1001, "参数错误"),
    RESOURCE_NOT_EXIST(1002, "资源不存在"),
    REPEATED_RESOURCE_NAME(1003, "资源名称已存在"),
    DEL_RESOURCE_FAIl(1004, "删除失败"),
    FILE_FORMAT_ERROR(1005, "文件格式不支持"),
    FILE_TOO_LARGE(1006, "文件大小超出限制"),
    WRONG_FORMAT(1007, "格式错误"),
    OUT_OF_LENGTH(1008, "超出长度");


    public Integer code;
    public String msg;

    CommonResponse(Integer code, String msg) {
        this.msg = msg;
        this.code = code;
    }
}
