# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 基类封装webdriver方法,方便调用,减少代码重复
import random
import time

import allure
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Commons.log_process import LogProcess
from Commons.logs import Log
from Commons.return_time import ReturnTime
from ConfigFile.contants_test import *


class BasicPage:
    # 图片文件夹路径
    __img_dir = LogProcess().get_log_dir()[1]

    def __init__(self, driver):
        self.driver: webdriver.Chrome = driver

    # 进入指定连接
    def get_url(self, url):
        self.driver.get(url=url)

    def get_current_url_path(self):
        """
        获取当前页面的url的路径
        :return: url路径
        """
        current_url = self.driver.current_url
        return current_url

    def set_img_error(self):
        """
        用例执行失败截图,并且加入allure测试报告中
        :return: 无返回值
        """
        # 获取图片存储的文件夹
        __time_tag = ReturnTime.get_Timestamp()
        __img_path = self.__img_dir + f"/{__time_tag}.png"
        try:
            # 进行截图
            self.driver.save_screenshot(filename=__img_path)
            Log.error(f"截图成功文件名称为：{__time_tag}.png")
            __file = open(__img_path, "rb").read()
            allure.attach(__file, "用例执行失败截图", allure.attachment_type.PNG)
        except Exception as e:
            Log.error(f"执行失败截图未能正确添加进入测试报告:{e}")
            raise e

    # 用例执行完毕截图，并且将截图加入allure测试报告中
    def set_img_case(self):
        """
        用例执行完毕截图，并且将截图加入allure测试报告中
        :return: 无返回值
        """
        with allure.step("关键步骤截图"):
            __img_name = ReturnTime.get_Timestamp()
            __img_path = self.__img_dir + f"/{__img_name}.png"
            try:
                # 截图前等待1秒防止图片没有正常加载
                time.sleep(1)
                self.driver.save_screenshot(filename=__img_path)
                Log.debug(f"用例执行完成，截图成功，文件名称为{__img_name}.png")
                # 读取图片信息
                __file = open(file=__img_path, mode="rb").read()
                allure.attach(__file, "关键步骤截图", allure.attachment_type.PNG)
            except Exception as e:
                Log.error(f"测试结果截图，未能正确添加进入测试报告:{e}")
                raise e

    # 元素染色
    def element_dyeing(self, element) -> None:
        """
        将被操作的元素染色
        :rollback: 是否将元素回滚
        :return: None
        """
        self.driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",
                                   element)

    # 等待元素可见
    def __wait_element_visible(self, model, locator):
        """
        等待元素可见
        :param model: 元素所处的页面
        :param locator: 元素定位表达式
        :return: 无返回值
        """
        Log.debug(f"-开始-等待页面{model}的元素：{locator}可见")
        try:
            # 获取等待开始时间的时间戳
            __start_time = ReturnTime.get_Timestamp()
            WebDriverWait(self.driver, timeout=WAIT_ELEMENT, poll_frequency=POLL_ELEMENT) \
                .until(ec.visibility_of_element_located(locator=locator))
            # 计算元素等待的时间
            __wait_time = ReturnTime.get_Timestamp() - __start_time
            Log.debug(f"页面：{model}上的元素{locator}已可见，共计等待{__wait_time:0.2f}秒")
        except TimeoutException:
            Log.error(f"页面：{model},等待元素{locator}超时")
            self.set_img_error()
            raise TimeoutException('元素等待超时')
        except InvalidSelectorException as e:
            Log.error(f"页面:{model},元素不可见或定位表达式:{locator}异常\n {e}")
            raise InvalidSelectorException('元素定位异常')

    # 等待元素可点击
    def __wait_element_clickable(self, model, locator):
        """
        等待元素点击
        :param model: 元素所处的页面
        :param locator: 元素定位表达式
        :return: 无返回值
        """
        Log.debug(f"-开始-等待页面{model}的元素：{locator}可点击")
        try:
            # 获取等待开始时间的时间戳
            __start_time = ReturnTime.get_Timestamp()
            WebDriverWait(self.driver, timeout=WAIT_ELEMENT, poll_frequency=POLL_ELEMENT) \
                .until(ec.element_to_be_clickable(locator=locator))
            # 计算元素等待的时间
            __wait_time = ReturnTime.get_Timestamp() - __start_time
            Log.debug(f"页面：{model}上的元素{locator}已可点击，共计等待{__wait_time:0.2f}秒")
        except TimeoutException as e:
            Log.error(f"页面：{model},等待元素{locator}超时")
            self.set_img_error()
            raise e
        except InvalidSelectorException as e:
            Log.error(f"页面:{model},元素不可点击或定位表达式:{locator}异常\n {e}")
            raise e

    # 等待元素存在
    def __wait_element_exit(self, model, locator):
        """
        等待元素存在
        :param model: 元素所处的页面
        :param locator: 元素定位表达式
        :return: 无返回值
        """
        Log.debug(f"-开始-等待页面{model}的元素：{locator}存在")
        try:
            # 获取等待开始时间的时间戳
            __start_time = ReturnTime.get_Timestamp()
            WebDriverWait(self.driver, timeout=WAIT_ELEMENT, poll_frequency=POLL_ELEMENT).until(
                ec.presence_of_element_located(locator=locator))
            # 计算元素等待的时间
            __wait_time = ReturnTime.get_Timestamp() - __start_time
            Log.debug(f"页面：{model}上的元素{locator}已存在，共计等待{__wait_time:0.2f}秒")
        except TimeoutException as e:
            Log.error(f"页面：{model},等待元素{locator}超时")
            self.set_img_error()
            raise e
        except InvalidSelectorException as e:
            Log.error(f"页面:{model},元素不存在或定位表达式:{locator}异常\n {e}")
            raise e

    # 等待元素不可见
    def wait_element_not_visible(self, model, locator):
        """
        等待元素不可见
        :param model: 元素所处的页面
        :param locator: 元素定位表达式
        :return: 无返回值
        """
        Log.debug(f"-开始-等待页面{model}的元素：{locator}存在")
        try:
            # 获取等待开始时间的时间戳
            __start_time = ReturnTime.get_Timestamp()
            time.sleep(1)
            WebDriverWait(self.driver, timeout=WAIT_ELEMENT,
                          poll_frequency=POLL_ELEMENT).until(ec.invisibility_of_element_located(locator=locator))
            # 计算元素等待的时间
            __wait_time = ReturnTime.get_Timestamp() - __start_time
            Log.debug(f"页面：{model}上的元素{locator}已经不可见，共计等待{__wait_time:0.2f}秒")
        except TimeoutException as e:
            Log.error(f"页面：{model},等待元素{locator}不可见超时")
            self.set_img_error()
            raise e
        except InvalidSelectorException as e:
            Log.error(f"页面:{model},元素不存在或定位表达式:{locator}异常\n {e}")
            raise e

    # 选择元素定位的等待方式
    def __select_wait_method(self, model, locator, mode="visible"):
        """
        选择元素定位的等待方式
        :param model: 传参定位的是哪个页面 字符串形式
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param mode: visible(元素可见), exist(元素存在),click(元素可点击)
        :return: 无返回值
        """
        if mode == "visible":
            self.__wait_element_visible(model=model, locator=locator)
        elif mode == "exist":
            self.__wait_element_exit(model=model, locator=locator)
        elif mode == "click":
            self.__wait_element_clickable(model=model, locator=locator)
        else:
            Log.error(f"定位{model}页面的元素:{locator},mode参数传值异常,入参值为：{mode}")

    # 元素定位
    def find_element(self, locator: tuple, mode="visible", model=None):
        """
        定位元素，支持所有定位单个元素的定位表达式
        :param model: 传参定位的是哪个页面 字符串形式
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param mode: visible(元素可见), exist(元素存在)
        :return: 定位到的元素对象
        """
        self.__select_wait_method(model=model, locator=locator, mode=mode)
        try:
            Log.debug(f"正在定位{model}页面的: {locator} 的元素")
            element = self.driver.find_element(*locator)
            self.element_dyeing(element=element)
            return element
        except TimeoutException:
            Log.error(f"页面:{model},定位元素:{locator}定位超时")
            self.set_img_error()
            raise TimeoutException("元素定位超时请检查")
        except Exception:
            Log.error(f"页面:{model},定位元素:{locator}定位失败")
            self.set_img_error()
            raise Exception("元素定位失败请检查")

    # 定位一组元素
    def find_elements(self, locator: tuple, mode="visible") -> list:
        """
        定位一组元素，返回一个列表
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param mode: visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        :return: 返回一组元素是一个列表
        """
        model = self.get_current_url_path()
        self.__select_wait_method(model=model, locator=locator, mode=mode)
        try:
            Log.debug(f"正在定位{model}页面的: {locator} 的元素")
            element_list = self.driver.find_elements(*locator)
            return element_list
        except Exception as e:
            Log.error(f"页面:{model},定位元素:{locator}定位失败")
            self.set_img_error()
            raise e

    # 将元素移动到页面可见区域
    def __move_element_visible(self, model, locator, element, alignment=False):
        """
         将元素移动到页面可见区域
        :param model: 传参定位的是哪个页面 字符串形式
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param alignment 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param element 需要可见的元素
        :return: 无返回值
        """
        Log.debug(f'将{model}页面的元素:{locator}移动至浏览器可见区域')
        try:
            # 代码执行比页面渲染速度快 这里放0.5秒等待页面渲染
            time.sleep(0.5)
            self.driver.execute_script('arguments[0].scrollIntoView({0});'.format(alignment), element)
            # 休眠1秒让页面可以正常滚动到对应的位置再执行下去
            time.sleep(1)
        except Exception as e:
            Log.error(f"{model}页面的元素:{locator}移动失败\n{e}")
            self.set_img_error()
            raise e

    # 点击元素
    def click_element(self, locator, mode="click", alignment=False, move_elemnet=False, is_double_click=False):
        """
        点击元素
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param mode: visible(元素可见),notvisible(元素消失不可见), exist(元素存在)，click(元素可点击)
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param move_elemnet: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :param is_double_click: False单击元素，传入True 双击元素
        :return: 无返回值
        """
        model = self.get_current_url_path()
        element = self.find_element(model=model, locator=locator, mode=mode)
        if move_elemnet is True:
            self.__move_element_visible(model=model, locator=locator,
                                        element=element, alignment=alignment)
        try:
            Log.debug(f"点击:{model}页面,属性为{locator}的元素")
            if is_double_click:
                ActionChains(self.driver).double_click(element).perform()
            else:
                element.click()
        except Exception as e:
            Log.error(f"页面{model}的元素: {locator} 点击失败")
            self.set_img_error()
            raise e

    # 随机点击一个元素
    def random_click_element(self, locator, num: int, mode="click", alignment=False, move_elemnet=False):
        """
        点击元素
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param num: 从第几位元素开始点击
        :param mode: visible(元素可见), exist(元素存在)，click(元素可点击)
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param move_elemnet: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :return: 点击的元素的文本
        """
        model = self.get_current_url_path()
        elements = self.find_elements(locator=locator, mode=mode)
        click_num: int = random.randint(num, len(elements) - 1)
        if move_elemnet is True:
            self.__move_element_visible(model=model, locator=locator,
                                        element=elements, alignment=alignment)
        try:
            element = elements[click_num]
            self.element_dyeing(element)
            Log.debug(f"点击:{model}页面,属性为{locator}的元素中的{click_num}位")
            element.click()
        except Exception as e:
            Log.error(f"页面{model}的元素: {locator} 中的第{click_num}位元素点击失败")
            self.set_img_error()
            raise e
        return element.text

    # 输入文本内容
    def input_text(self, locator, content, mode="visible", alignment=False, move_elemnet=False):
        """
        输入文本内容
        :param locator: 传入元素定位表达式
        :param content: 传入输入的文本内容
        :param mode:  visible(元素可见), exist(元素存在)
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param move_elemnet: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :return: 无返回值
        """
        model = self.get_current_url_path()
        element = self.find_element(model=model, locator=locator, mode=mode)
        if move_elemnet is True:
            self.__move_element_visible(model=model, locator=locator,
                                        element=element, alignment=alignment)
        try:
            Log.debug(f"输入操作:{model}页面下的属性为:{locator}的元素,输入内容为{content}")
            element.send_keys(content)
            self.driver.execute_script(
                "arguments[0].setAttribute('style', 'background: write; border: 1px solid black;');", element)
        except Exception as e:
            self.set_img_error()
            Log.error(f"页面{model}的属性: {locator} 输入操作失败")
            raise e
        return element

    # 清除内容
    def clear_contents(self, locator, mode="visible", alignment=False, move_elemnet=False):
        """
        清除文本内容
        :param locator: 传入元素定位表达式
        :param mode:  visible(元素可见), exist(元素存在)
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param move_elemnet: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :return: 无返回值
        """
        model = self.get_current_url_path()
        element = self.find_element(model=model, locator=locator, mode=mode)
        if move_elemnet is True:
            self.__move_element_visible(model=model, locator=locator,
                                        element=element, alignment=alignment)
        try:
            Log.debug(f"输入操作:{model}页面下的属性为:{locator}的元素,清除内容")
            element.clear()
        except Exception as e:
            self.set_img_error()
            Log.error(f"页面{model}的属性: {locator} 清除操作失败")
            raise e

    # 获取元素的文本内容
    def get_element_text(self, locator, mode='visible', alignment=False, move_elemnet=False):
        """
        获取元素的文本内容
        :param locator:  传入元素定位表达式
        :param mode: visible(元素可见), exist(元素存在)
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param move_elemnet: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :return: 返回获取到的元素文本内容
        """
        model = self.get_current_url_path()
        element = self.find_element(model=model, locator=locator, mode=mode)
        if move_elemnet is True:
            self.__move_element_visible(model=model, locator=locator,
                                        element=element, alignment=alignment)
        try:
            Log.debug(f"文本获取操作:获取{model}页面下的属性为:{locator}的元素的文本内容")
            return element.text
        except Exception as e:
            Log.error(f"页面{model}的元素:{locator}获取文本操作失败")
            self.set_img_error()
            raise e

    # 复选框内容点击
    def click_radios(self, locator, method, amount=None, mode='visible', alignment=False, move_elemnet=False):
        """
        复选框内容点击
        :param locator: 传入元素定位表达式
        :param mode:  visible(元素可见), exist(元素存在)
        :param amount: 传入复选项的数量 例子如果是3个选项就传入3
        :param method: 选择对应的内容选择方式 all 点击复选框的全部内容 random 随机点击复选框的中的某一个选项 assign点击指定的某个复选项
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param move_elemnet: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :return: 全部点击时无返回，其他返回被点击的元素
        """
        # 定位到复选框一定是一组元素
        model = self.get_current_url_path()
        elements = self.find_elements(locator=locator, mode=mode)
        if move_elemnet is True:
            self.__move_element_visible(model=model, locator=locator,
                                        element=elements, alignment=alignment)
        try:
            Log.debug('点击方式为：{}'.format(method))
            if method == 'all':
                # 点击复选项中每一个元素
                for ele in elements:
                    ele.click()
            # 随机点击复选项中的某一个内容
            elif method == 'random':
                # 导入随机数包
                import random
                # 生成指定范围之内的随机数作为需要点击的radio
                num = random.randint(0, amount - 1)
                element = elements[num].click()
                # 返回被点击的元素
                return element
            # 点击复选框中指定位置的选项
            elif method == 'assign':
                # 因为从0开始计数，所以传入的 amount-1
                element = elements[amount - 1].click()
                return element
            else:
                Log.error('点击方式输入错误，请检查')
        except Exception as e:
            Log.error(f"页面{model}的元素:{locator}复选框点击操作失败")
            self.set_img_error()
            raise e

    # 判断元素是否勾选
    @staticmethod
    def element_is_selected(elenmet):
        """
        判断元素是否勾选
        :param elenmet: 需要校验是否勾选的元素
        :return: 选中是Ture 没有选择是False
        """
        return elenmet.is_selected()

    # 选择下拉菜单中的内容
    def select_contents_menu(self, locator, text, mode='visible', alignment=False, move_elemnet=False):

        """
        选择下拉菜单中的内容
        :param locator: 传入元素定位表达式
        :param text: 出入下拉列表需要选择的内容
        :param mode: visible(元素可见), exist(元素存在)
        :param alignment:  默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param move_elemnet: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        """
        model = self.get_current_url_path()
        element = self.find_element(model, locator, mode)
        # 定义一个存储菜单内容的空列表
        option = []
        if move_elemnet is True:
            self.__move_element_visible(model=model, locator=locator, element=element, alignment=alignment)
        try:
            # 获取下拉列表的内容
            options = element.find_elements_by_tag_name("option")
            for value in options:
                option.append(value)
            if text in option:
                Select(element).select_by_visible_text(text)
            else:
                Log.error(f"选项:{text}不在下拉列表之中请检查")
        except Exception as e:
            self.set_img_error()
            Log.error(f"页面{model}的元素:{locator}下拉框操作失败请检查")
            raise e

    # 处理页面alert
    def dispose_alert(self, action):
        """
        处理页面alert
        :param action: 参数为 accept 点击alert的确定 dismiss点击alert的取消
        :return: 返回alert的文本内容 可能有些用例需要用这个参数去校验
        """
        # 等待alert出现再去操作
        WebDriverWait(driver=self.driver, timeout=WAIT_ELEMENT, poll_frequency=POLL_ELEMENT).until(
            ec.alert_is_present())
        alert = self.driver.switch_to.alert
        # 尝试点击alert
        try:
            if action == 'accept':
                alert.accept()
            elif action == 'dismiss':
                alert.dismiss()
            else:
                Log.error('alert 处理参数错误请检查')
            return alert.text
        except Exception as e:
            Log.error('alert处理异常')
            raise e

    # 获取当前页面的句柄
    def get_handles(self):
        """
        获取当前页面的句柄
        :return: 方法返回值当前获取到的句柄值
        """
        # 获取当前页面的句柄
        handles = self.driver.window_handles
        return handles

    # 浏览器页面切换--通过切换句柄实现切换到正在使用的页面上
    def swich_window(self, old_handle):
        """
        浏览器页面切换--通过切换句柄实现切换到正在使用的页面上
        :param old_handle: 传入之前获取的句柄的值
        :return:
        """
        # 等待最新的窗口出现
        WebDriverWait(driver=self.driver, timeout=WAIT_ELEMENT, poll_frequency=POLL_ELEMENT).until(
            ec.new_window_is_opened(old_handle))
        # 调用获取句柄的方法拿到最新打开的标签页的句柄
        new = self.get_handles()
        # 切换到最新页面因为时最新所以直接使用下标 -1 就行
        self.driver.switch_to.window(new[-1])

    # 判断单元素是否存在
    def is_element_exist(self, locator, timeout=10):
        """
        判断单元素是否存在
        :param timeout: 默认超时时间
        :param locator: 传入元素定位表达式
        :return: 返回布尔值 true表示元素存在 false表示元素不存在
        """
        model = self.get_current_url_path()
        try:
            Log.debug(f'判断{model}页面的元素{locator}是否存在')
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.1).until(ec.visibility_of_element_located(locator=locator))
            return True
        except Exception:
            return False

    # 判断元素是否已经消失不见了
    def element_whether_invisibility(self, locator):
        model = self.get_current_url_path()
        try:
            # 主要用于处理loading页面加载完成后1秒再去判断保证被判断的元素正常展示
            # time.sleep(1)
            # 获取等待开始时间的时间戳
            __start_time = ReturnTime.get_Timestamp()
            Log.debug(f'判断{model}页面的元素{locator}是否消失了')
            WebDriverWait(self.driver, timeout=60, poll_frequency=0.1).until(
                ec.invisibility_of_element_located(locator=locator))
            # 计算元素等待的时间
            __wait_time = ReturnTime.get_Timestamp() - __start_time
            Log.debug(f"页面：{model}上的元素{locator}已消失，共计等待{__wait_time:0.2f}秒")
            return True
        except Exception:
            return False

    # 切换ifram
    def switch_ifram(self, locator):
        """
        判切换ifram，部分页面的元素在ifram里需要切换后定位
        :param locator: 传入元素定位表达式
        """
        model = self.get_current_url_path()
        try:
            Log.debug(f'切换{model}页面的ifram{locator}')
            self.driver.switch_to.frame(frame_reference=self.find_element(model=model, locator=locator))
        except Exception:
            Log.error(f'{model}页面的ifram切换失败')

    # 鼠标悬停
    def mouse_over(self, locator, times) -> None:
        """
        鼠标悬停功能
        :param locator: 元素定位表达式
        :param times: 悬停时间
        :return: None
        """
        model = self.get_current_url_path()
        element = self.find_element(model=model, locator=locator)
        ActionChains(self.driver).move_to_element(to_element=element).perform()
        time.sleep(times)
