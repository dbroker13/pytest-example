from appium import webdriver
from os import path
import pytest
import yaml

from appium.options.common import AppiumOptions

CUR_DIR = path.dirname(path.abspath(__file__))
# YAML_CONFIG = path.join(CUR_DIR, '..', 'mobile', 'app-release.apk')
YAML_CONFIG = path.join(CUR_DIR, 'config.yaml')
def load_yaml():
    config = ""
    with open(YAML_CONFIG, 'r') as file:
        config=  yaml.safe_load(file)
        print(config)
        return config
    
def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='ios')

@pytest.fixture(scope='class')
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError('--platform value must be ios or android')
    return plat

# def pytest_configure(config):
#     myvalue = config.getini('my_option')
#     print(myvalue)

# APPIUM = 'https://dev-us-sny-1.headspin.io:7030/v0/<api-key>/wd/hub'
#APPIUM = 'https://dev-us-sny-4.headspin.io:7017/v0/03e48a3884fb4707a448f4480a87600e/wd/hub'
@pytest.fixture
def ios_driver():
    config = load_yaml()
    api_token = config['server']['api_token']
    url = config['server']['url']
    APPIUM = f'{url}/v0/{api_token}/wd/hub'
    CAPS = {
    "automationName": "xcuitest",
    "platformVersion": "15.7",
    "platformName": "ios",
    "deviceName": "iPhone 12 Mini",
    'browserName': 'Safari',
    "udid": "00008101-000470E61438001E"
}
    driver = webdriver.Remote(
        command_executor=APPIUM,
        desired_capabilities=CAPS
    )
    yield driver
    #could keep executing code after its done
    driver.quit()

@pytest.fixture(scope='class')
def android_driver(platform):
    config = load_yaml()
    api_token = config['server']['api']
    url = config['server']['url']
    APPIUM = f'{url}/v0/{api_token}/wd/hub'
    CAPS = config['android_caps']
    android_driver = webdriver.Remote(
        command_executor=APPIUM,
        options=AppiumOptions().load_capabilities(CAPS))
    # android_driver = webdriver.Remote(
    #     command_executor=APPIUM,
    #     desired_capabilities=CAPS
    # )
    yield android_driver
    #could keep executing code after its done
    android_driver.quit()


# @pytest.fixture
# def driver(platform):
#     config = load_yaml()
#     api_token = config['server']['api']
#     url = config['server']['url']
#     APPIUM = f'{url}/v0/{api_token}/wd/hub'
#     platform = 'android'
#     print(platform)
#     if platform == 'ios':
#         CAPS = config['ios_caps']
#     else:
#         CAPS = config['web_android_caps']
#     print(CAPS)
#     driver = webdriver.Remote(
#         command_executor=APPIUM,
#         desired_capabilities=CAPS
#     )
#     yield driver
#     #could keep executing code after its done
#     driver.quit()

@pytest.fixture
def driver(platform):
    config = load_yaml()
    api_token = config['server']['api']
    url = config['server']['url']
    APPIUM = f'{url}/v0/{api_token}/wd/hub'
    platform = 'android'
    print(platform)
    if platform == 'ios':
        CAPS = config['ios_caps']
    else:
        CAPS = config['web_android_caps']
    print(CAPS)
    driver = webdriver.Remote(
        command_executor=APPIUM,
        options=AppiumOptions().load_capabilities(CAPS))
    yield driver
    #could keep executing code after its done
    driver.quit()