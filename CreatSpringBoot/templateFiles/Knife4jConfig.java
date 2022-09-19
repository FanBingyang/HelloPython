package com.byfan.springboottemplate.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2WebMvc;

/**
 * @Description swagger文档
 * @Author: byfan
 * @Date:
 */
@Configuration
@EnableSwagger2WebMvc
public class Knife4jConfig {
    @Bean(value = "defaultApi2")
    public Docket createRestApi() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                .groupName("Springboottemplate项目接口文档")
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.byfan.springboottemplate"))
                .paths(PathSelectors.any())
                .build();
    }

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("Springboottemplate项目接口文档")
                .description("Springboottemplate项目接口文档")
                .termsOfServiceUrl("http://127.0.0.1:9000/")
                .contact(new Contact("byfan","byfanx@163.com","http://byfan.xyz"))
                .version("1.0")
                .build();
    }

}