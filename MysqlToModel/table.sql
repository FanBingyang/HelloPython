CREATE TABLE `ide_extension_package` (
  `id` int(11) NOT NULL COMMENT '主键',
  `name` varchar(50) CHARACTER SET utf8mb4 NOT NULL COMMENT '插件名publisher.name',
  `version` varchar(50) NOT NULL COMMENT '版本号',
  `author` varchar(50) DEFAULT NULL COMMENT '开发者',
  `publisher` varchar(50) NOT NULL COMMENT '发布人',
  `url` varchar(500) NOT NULL COMMENT '插件存储地址',
  `description` text NOT NULL COMMENT '插件描述信息',
  `status` tinyint(1) NOT NULL COMMENT '状态：-1 删除   0 停用  1 使用',
  `create_user` varchar(50) NOT NULL COMMENT '创建人',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='插件包详情';