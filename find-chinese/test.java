package com.gitee.opera.controller;

import com.gitee.opera.bean.BaseOrder;
import com.gitee.opera.bean.PageData;
import com.gitee.opera.bean.PageQuery;
import com.gitee.opera.bean.query.AgentQuery;
import com.gitee.opera.bean.vo.*;
import com.gitee.opera.common.BaseResponse;
import com.gitee.opera.common.Constants;
import com.gitee.opera.enums.BaseResponseEnum;
import com.gitee.opera.model.Agent;
import com.gitee.opera.sa.api.entity.monitor.AgentInfoRedisBean;
import com.gitee.opera.service.IAgentService;
import io.swagger.annotations.*;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import springfox.documentation.annotations.ApiIgnore;

import javax.validation.Valid;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * @ClassName AgentController
 * @Description 主机相关业务模块
 * @Author ZhangChao
 * @Date 2022/5/27
 */
@Slf4j
@Api(tags = "主机相关业务模块")
@RestController
@RequestMapping("/rest/v1/agent")
public class AgentController {

    @Autowired
    IAgentService iAgentService;

    @SneakyThrows
    @ApiOperation("主机信息分页查询")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "currentPage", value = "当前页", paramType = "query", required = true, dataType = "int"),
            @ApiImplicitParam(name = "pageSize", value = "每页数据条数", paramType = "query", required = true, dataType = "int"),
            @ApiImplicitParam(name = "orderByList", value = "排序字段，多个用英文逗号分隔", paramType = "query", allowMultiple = true, required = false, dataType = "string"),
            @ApiImplicitParam(name = "ascOrDescList", value = "asc或desc，多个用英文逗号分隔", paramType = "query", allowMultiple = true, required = false, dataType = "string"),
            @ApiImplicitParam(name = "name", value = "主机名称", paramType = "query", required = false, dataType = "string"),
            @ApiImplicitParam(name = "type", value = Constants.SYSTEM_ALL_TYPES, paramType = "query", required = false, dataType = "int"),
            @ApiImplicitParam(name = "ip", value = "主机ip", paramType = "query", required = false, dataType = "string"),
            @ApiImplicitParam(name = "os", value = "主机操作系统类型", paramType = "query", required = false, dataType = "string"),
            @ApiImplicitParam(name = "statusList", value = Constants.AGENT_ALL_STATUS, paramType = "query",allowMultiple = true, required = false, dataType = "int"),
            @ApiImplicitParam(name = "labelId", value = "当前主机组ID", paramType = "query", required = false, dataType = "int"),
            @ApiImplicitParam(name = "agentIdList", value = "主机id列表", paramType = "query",allowMultiple = true, required = false, dataType = "int"),

    })
    @GetMapping("/infos")
    public BaseResponse<PageData<AgentDetailVo>> queryByPage(@RequestParam(required = false) Integer currentPage,
                                                             @RequestParam(required = false, defaultValue = "10") Integer pageSize,
                                                             @RequestParam(required = false) List<String> orderByList,
                                                             @RequestParam(required = false) List<String> ascOrDescList,
                                                             @RequestParam(required = false) String name,
                                                             @RequestParam(required = false) Integer type,
                                                             @RequestParam(required = false) String ip,
                                                             @RequestParam(required = false) String os,
                                                             @RequestParam(required = false) List<Integer> statusList,
                                                             @RequestParam(required = false) Long labelId,
                                                             @RequestParam(required = false) List<Long> agentIdList) {

        PageQuery pageQuery = new PageQuery(currentPage, pageSize);
        if (orderByList != null && ascOrDescList != null && orderByList.size() == ascOrDescList.size() && ascOrDescList.size() > 0) {
            List<BaseOrder> orderList = new ArrayList<>();
            for (int i = 0; i < orderByList.size(); i++) {
                BaseOrder order = new BaseOrder(orderByList.get(i), ascOrDescList.get(i));
                orderList.add(order);
            }
            pageQuery.setOrderList(orderList);
        }

        AgentQuery query = new AgentQuery();
        query.setName(name);
        query.setStatusList(statusList);
        query.setType(type);
        query.setLabelId(labelId);
        query.setIp(ip);
        query.setOs(os);
        query.setPageQuery(pageQuery);
        query.setAgentIdList(agentIdList);

        PageData<AgentDetailVo> data = iAgentService.queryPageList(query);
        BaseResponse response = new BaseResponse(BaseResponseEnum.OK, data);
        return response;
    }

    @ApiIgnore
    @SneakyThrows
    @ApiOperation(value = "创建主机")
    @ApiImplicitParams({
    })
    @RequestMapping(value = "/", method = RequestMethod.POST)
    public BaseResponse<Agent> createAgent(@Valid @RequestBody AgentAddVo agentAddVo) {
        Agent data = iAgentService.createAgent(agentAddVo);
        BaseResponse response = new BaseResponse(BaseResponseEnum.OK, data);
        return response;
    }

    @SneakyThrows
    @ApiOperation(value = "编辑主机")
    @ApiImplicitParams({
    })
    @RequestMapping(value = "/", method = RequestMethod.PUT)
    public BaseResponse<Agent> createAgent(@Valid @RequestBody AgentUpdateVo agentUpdateVo) {
        Agent data = iAgentService.updateAgent(agentUpdateVo);
        BaseResponse response = new BaseResponse(BaseResponseEnum.OK, data);
        return response;
    }

    @SneakyThrows
    @ApiOperation(value = "移除主机")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "password", value = "密码", paramType = "query", required = true, dataType = "string"),
            @ApiImplicitParam(name = "idList", value = "主机id集合", paramType = "query", allowMultiple = true, required = true, dataType = "int"),
    })
    @RequestMapping(value = "/", method = RequestMethod.DELETE)
    public BaseResponse deleteAgent(@RequestParam String password, @RequestParam List<Long> idList) {
        return BaseResponse.success(Map.of("failures", iAgentService.delete(password, idList)));
    }

    /**
     * @Description 查看主机详情
     * @Author byfan
     * @Date 2022/6/22 17:37
     * @param uuid
     * @return com.gitee.opera.common.BaseResponse
     * @throws
     */
    @SneakyThrows
    @ApiOperation("查看主机详情")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "uuid", value = "主机uuid", required = true, paramType = "path", dataType = "String")
    })
    @GetMapping("/{uuid}")
    public BaseResponse<AgentVo> getAgent(@PathVariable String uuid){
        AgentVo agentVo = iAgentService.getAgentByUuid(uuid);
        BaseResponse<AgentVo> response = new BaseResponse(BaseResponseEnum.OK, agentVo);
        return response;
    }

    @SneakyThrows
    @ApiOperation("查看主机规格信息")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "uuid", value = "主机uuid", required = true, paramType = "path", dataType = "String")
    })
    @GetMapping("/host/{uuid}")
    public BaseResponse<AgentHostInfoVo> getAgentInfo(@PathVariable String uuid){
        AgentHostInfoVo agentHostInfoVo = iAgentService.getAgentHostInfoByUuid(uuid);
        BaseResponse<AgentHostInfoVo> response = new BaseResponse(BaseResponseEnum.OK, agentHostInfoVo);
        return response;
    }

    @SneakyThrows
    @ApiOperation(value = "批量修改主机所属分组")
    @ApiImplicitParams({
    })
    @RequestMapping(value = "/label", method = RequestMethod.PUT)
    public BaseResponse<String> createAgent(@Valid @RequestBody AgentLabelUpdateVo agentUpdateVo) {
        iAgentService.updateAgentLabel(agentUpdateVo);
        BaseResponse response = new BaseResponse(BaseResponseEnum.OK,BaseResponseEnum.OK.name());
        return response;
    }

    @SneakyThrows
    @ApiOperation("对外提供(pipe、opera)查询主机")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "serviceUnit", value = "服务单元  1:Pipe  2:Deploy  3:Opera", required = true, paramType = "query", dataType = "int"),
            @ApiImplicitParam(name = "type", value = "主机类型  1: Windows  2: Linux", required = true, paramType = "query", dataType = "int"),
            @ApiImplicitParam(name = "agentName", value = "主机名称", required = false, paramType = "query", dataType = "string")
    })
    @RequestMapping(value = "/query-agent", method = RequestMethod.GET)
    public BaseResponse<List<AgentForProvideVo>> queryAgent(@RequestParam Integer serviceUnit,
                                                            @RequestParam Integer type,
                                                            @RequestParam(required = false) String agentName){
        List<AgentForProvideVo> agents = iAgentService.queryAgent(serviceUnit, type, agentName);
        BaseResponse<List<AgentForProvideVo>> response = new BaseResponse(BaseResponseEnum.OK, agents);
        return response;
    }

    @SneakyThrows
    @ApiOperation("根据主机组id查询主机列表id")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "labelId", value = "主机组id", required = true, paramType = "path", dataType = "int")
    })
    @RequestMapping(value = "/{labelId}/ids", method = RequestMethod.GET)
    public BaseResponse<List<Long>> getAgentIdsByLabelId(@PathVariable Integer labelId) {
        List<Long> agentIds = iAgentService.getAgentIdsByLabelId(labelId);
        BaseResponse<List<Long>> response = new BaseResponse(BaseResponseEnum.OK, agentIds);
        return response;
    }

}
