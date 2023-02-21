/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : maoxioachen

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 18/11/2022 18:55:40
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for adjust_class
-- ----------------------------
DROP TABLE IF EXISTS `adjust_class`;
CREATE TABLE `adjust_class`  (
  `direction` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `i_time` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `l_time` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `reason` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of adjust_class
-- ----------------------------
INSERT INTO `adjust_class` VALUES ('全栈', '宁玉琰', '11月18日第2大节', '11月18日第3大节', '饿了');
INSERT INTO `adjust_class` VALUES ('秘书处', '余雨竹', '11月18日第4大节', '11月18日第3大节', '吃饭睡觉打豆豆！');

-- ----------------------------
-- Table structure for leave_from
-- ----------------------------
DROP TABLE IF EXISTS `leave_from`;
CREATE TABLE `leave_from`  (
  `direction` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `time` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `reason` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of leave_from
-- ----------------------------
INSERT INTO `leave_from` VALUES ('人工智能', '张雪涵', '11月16日第1大节', '早上体测呢');
INSERT INTO `leave_from` VALUES ('人工智能', '王泽宇', '11月18日第4大节', '睡午觉');
INSERT INTO `leave_from` VALUES ('人工智能', '王智申', '11月16日第1大节', '节目排练');
INSERT INTO `leave_from` VALUES ('人工智能', '王宇舟', '11月18日第4大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('人工智能', '郝少敏', '11月16日第1大节', '体测');
INSERT INTO `leave_from` VALUES ('人工智能', '王溪慈', '11月16日第2大节', '体测');
INSERT INTO `leave_from` VALUES ('人工智能', '郝少敏', '11月16日第1大节', '体测');
INSERT INTO `leave_from` VALUES ('人工智能', '张硕航', '11月16日第3大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('人工智能', '郝少敏', '11月16日第1大节', '体测');
INSERT INTO `leave_from` VALUES ('人工智能', '郭鸿凯', '11月18日第4大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('人工智能', '郭鸿凯', '11月18日第4大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('人工智能', '陈新阳', '11月16日第4大节', '睡午觉');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈建设叽');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月18日第4大节', '文科男哈啊哈建设叽加');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈建设叽加');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈建设叽加');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈建设叽加');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈建设叽加');
INSERT INTO `leave_from` VALUES ('人工智能', '王鹏超', '11月18日第4大节', '开会');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈建设叽加');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月18日第4大节', '文科男哈啊哈');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈哈哈');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '文科男哈啊哈');
INSERT INTO `leave_from` VALUES ('Java', '郭树鑫', '11月16日第4大节', '下午要上体育课，身体有点不舒服，想上午休息调整一下');
INSERT INTO `leave_from` VALUES ('人工智能', '郭鸿凯', '11月16日第4大节', '老师调课啦');
INSERT INTO `leave_from` VALUES ('人工智能', '谢伟', '11月18日第4大节', '要开学委会');
INSERT INTO `leave_from` VALUES ('全栈', '宁玉琰', '11月18日第4大节', '下午体测');
INSERT INTO `leave_from` VALUES ('人工智能', '雷蒙阳', '11月18日第1大节', '体测');
INSERT INTO `leave_from` VALUES ('秘书处', '余雨竹', '11月18日第4大节', '我妈喊我回家吃饭');
INSERT INTO `leave_from` VALUES ('秘书处', '余雨竹', '11月18日第3大节', '我妈喊我回家吃饭');
INSERT INTO `leave_from` VALUES ('秘书处', '余雨竹', '11月18日第1大节', '我妈喊我回家吃饭');

-- ----------------------------
-- Table structure for yd_work
-- ----------------------------
DROP TABLE IF EXISTS `yd_work`;
CREATE TABLE `yd_work`  (
  `work_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `work_link` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of yd_work
-- ----------------------------
INSERT INTO `yd_work` VALUES ('qq机器人，go-cqhttp', 'https://docs.go-cqhttp.org/');
INSERT INTO `yd_work` VALUES ('腾讯智能聊天', 'https://cloud.tencent.com/document/product/1060/42602');
INSERT INTO `yd_work` VALUES ('AI七期作业情况-飞书共享文档', ' https://yundingshuyuan.feishu.cn/sheets/shtcn9gM1UhmkL6QiOiSJmIx8BG?sheet=fcba52');
INSERT INTO `yd_work` VALUES ('二维码生成页面（七期签到使用）', 'https://signin.snowhouse.space/#/UserPage');
INSERT INTO `yd_work` VALUES ('管理员签到页面（用于六期扫码，密码：ljq86488）', 'https://signin.snowhouse.space/#/');

-- ----------------------------
-- Table structure for yunzi_seven
-- ----------------------------
DROP TABLE IF EXISTS `yunzi_seven`;
CREATE TABLE `yunzi_seven`  (
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `direction` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `qq_number` char(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of yunzi_seven
-- ----------------------------
INSERT INTO `yunzi_seven` VALUES ('牛相前', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('邹传航', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('秦鹤亮', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('王睿', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('尚诚卓', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('谭锦远', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('董磊', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('张宇驰', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('葛迎旗', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('马鑫硕', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵晓虎', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('孔子杰', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('闫佳雪', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('王成滈', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘蓉蓉', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('张祐卿', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('张智恒', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('王晓雪', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('王嘉锐', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('郭卜溱', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('闫首廷', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('陈泽一', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('郝达峰', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('张俊祥', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵滢博', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('薛婧妍', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('贾书宇', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('陈哲', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('罗军', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('王瑞琛', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨华', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨佳宁', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨桓', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('辛未', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('李华程', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('王玉杰', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('陈鑫', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('张曦文', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵彦欣', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('侯威丞', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('李颖', 'CPU&OS', NULL);
INSERT INTO `yunzi_seven` VALUES ('戎晨杨', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('解卓衡', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('李嘉健', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('张振桦', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('胡旭鑫', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('王渊', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('王佳煜', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('姚睿杰', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('陈波翰', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('翟嘉乐', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('牛治宇', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('李柳含', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨越', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('徐天赋', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('卢一鸣', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('徐少华', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('郭世通', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('寻鑫研', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('胡孔', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('李菽薪', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘子颖', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('崔玉嵘', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('镡宇星', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('李朋逊', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('李昕怡', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('李婧', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('李贝', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('陈昶文', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('张治国', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('张恒磊', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('常江', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('陶枫', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('郭树鑫', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('任帅齐', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('南极洲', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('郑宇萍', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('李府成', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('王一森', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('郭慧娟', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨智杰', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('徐占悦', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('黄有杰', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('李欣悦', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('张徐瑞', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('孙陆鑫', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('沙羽轩', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('张洪玮', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵佳浩', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('王梦瑶', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('解耀轩', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('郝曦鹏', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('王铭杰', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('吴敬', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('王嘉乐', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('方世杰', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('郭奕博', 'Java', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘宇', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('余雨竹', '秘书处', '2910711781');
INSERT INTO `yunzi_seven` VALUES ('杜晨博', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('景敏潇', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('王璐瑶', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('鲍晓阳', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('高亭', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('史晓磊', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('冯思雨', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵靖涵', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('张璐', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('李钰', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘泽鹏', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('段菲菲', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('李若璇', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('姚逸群', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘怡杉', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('焦碧雪', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('吴锦茹', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('李嘉玲', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('史翊坤', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('王喆', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘念', '秘书处', NULL);
INSERT INTO `yunzi_seven` VALUES ('吕厚均', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨蕊瑞', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('李旭', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('史璐怡', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张清喆', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('邱泽茜', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('郑依锦', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('贾京浩', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('董赫赫', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张偲禹', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张滋婧', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('吕斌', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('梅嘉钦', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('王铭埔', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('黄雅贞', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('蔡正', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('黄泽熠', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('李建霆', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('高雅鑫', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张艺珑', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('李姝鑫', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('韩虹', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('王钰捷', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('李静怡', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('魏增辉', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('孙锦琦', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('王烁杰', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('田朵朵', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('穆亮艳', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张钦媛', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('段颖', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('宁凌帆', '全栈', '');
INSERT INTO `yunzi_seven` VALUES ('黄笑苒', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('薛江槟', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张云涛', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('谢光翔', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('宁玉琰', '全栈', '');
INSERT INTO `yunzi_seven` VALUES ('柳浩宇', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('罗梦玉', '全栈', '');
INSERT INTO `yunzi_seven` VALUES ('王家正', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('彭俊杰', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('李树勋', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张建亮', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('李嘉伟', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('任超毅', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('阎昱帆', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张然', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵丹娜', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('李艳芳', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵雨欣', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('孟验岩', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('夏阳洋', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨镜廷', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('马荣臻', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('米英杰', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('褚宇鑫', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('卢楠', '全栈', '');
INSERT INTO `yunzi_seven` VALUES ('张晏铭', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('边建强', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('梁嘉辉', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('李彬蔚', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('韩仪琼', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('郝孟奇', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张紫轩', '全栈', NULL);
INSERT INTO `yunzi_seven` VALUES ('张硕航', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('李峥', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('樊泓昱', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王健炫', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('郭时宇', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('张益德', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('封鑫田', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('冯雲', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('郭鸿凯', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('李喆', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('谢昊洋', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('任博轩', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('牛玮茗', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('何秉轩', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('李诗语', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨晨旭', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('张雪涵', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵佳宝', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王智申', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('解金洋', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘泽', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('吴彦兴', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('张春慧', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('郭淑娟', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘嘉琪', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王一帆', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王宇舟', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王君', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('夏景琦', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王彤', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('张明磊', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨焰琴', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('吴昊', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('张一超', '人工智能', '3369193332');
INSERT INTO `yunzi_seven` VALUES ('谢伟', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('于翔川', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('陈新阳', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('侯华润', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王泽宇', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨梅', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('李晓慧', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王玥', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘思洲', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('陈柔曼', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘荣鑫', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘清湲', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('张开然', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王鹏超', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('周毅涵', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵婷婷', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵文恺', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('郝少敏', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('王溪慈', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('李翼廷', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('行亚楠', '人工智能', NULL);
INSERT INTO `yunzi_seven` VALUES ('雷蒙阳', '人工智能', '3544308013');
INSERT INTO `yunzi_seven` VALUES ('郭玉秦', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('赵紫波', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('李舸帆', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('成轶轲', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('牛鑫鑫', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('倪益波', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('郝国强', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('李婷玉', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨庆科', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('樊雅欣', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('许翔杰', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('邓鑫岩', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('张羽乐', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('贾若楠', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('易崇天', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('林雅玲', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('温子涵', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('褚泽宇', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('段玉宇', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('王钟崎', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('刘慧琳', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('李林涛', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('杨舒婷', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('白晓凡', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('朱运林', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('闫婕妤', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES ('杜非凡', '设计', NULL);
INSERT INTO `yunzi_seven` VALUES (NULL, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
