
def add():
	pass


'''

CREATE TABLE `request_port` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `port_path` varchar(255) NOT NULL COMMENT '接口路径',
  `request_data` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '接口请求值',
  `response_data` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '接口返回值',
  `test_function` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '测试方法名',
  `error_data` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '错误响应值',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='接口集合';

'''

