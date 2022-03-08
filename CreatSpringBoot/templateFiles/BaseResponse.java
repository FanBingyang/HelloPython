package com.byfan.springboottemplate.common;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @Author: byfan
 * @Description 后端返回统一对象
 * @Version 1.0
 * @Date: 2021/12/8 21:29
 */
@ApiModel("基础返回对象")
@Data
public class BaseResponse<T> {

    @ApiModelProperty(name = "code", notes = "状态码")
    int code;

    @ApiModelProperty(name = "message", notes = "消息")
    String msg;

    @ApiModelProperty(name = "data", notes = "数据对象")
    T data;

    public BaseResponse() {
        this.code = CommonResponse.OK.code;
        this.msg = CommonResponse.OK.msg;
        this.data = null;
    }

    public BaseResponse(CommonResponse response) {
        this.code = response.code;
        this.msg = response.msg;
        this.data = null;
    }

    public BaseResponse(CommonResponse response, T data) {
        this.code = response.code;
        this.msg = response.msg;
        this.data = data;
    }

    public static <T> BaseResponse<T> success(T data) {
        final BaseResponse<T> response = new BaseResponse<>();
        response.setData(data);
        return response;
    }

    public static <Void> BaseResponse<Void> error() {
        final BaseResponse<Void> response = new BaseResponse<>();
        response.setCode(CommonResponse.UNKNOWN_ERROR.code);
        response.setMsg(CommonResponse.UNKNOWN_ERROR.msg);
        return response;
    }
}