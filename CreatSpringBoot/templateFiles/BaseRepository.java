package com.byfan.springboottemplate.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;

import java.io.Serializable;

/**
 * @Description 基础Dao类
 * @Author: byfan
 * @Date:
 */
@NoRepositoryBean
public interface BaseRepository<T,PK extends Serializable> extends JpaRepository<T,PK> {
}