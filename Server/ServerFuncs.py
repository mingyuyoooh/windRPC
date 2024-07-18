from datetime import datetime
from ServerUtils import CONSTANTS

    
"""
Server:  ServerFuncs.py

本文件包含了各个注册函数

"""

"""
计算函数
"""
def add(*args,**kwargs):
    """
    ADD A+B+C+...
    """
    try:
        print(f"[INFO] add function is called with args = {args} and kwargs = {kwargs}")
        ans = 0
        for arg in args:
            ans+=arg
        return ans
    except Exception as e:
        print(f"[ERROR] Fail to call add function:{e} ")
        return None
def minus(*args,**kwargs):
    """
    MINUS A-B-C-...
    """
    try:
        print(f"[INFO] minus function is called with args = {args} and kwargs = {kwargs}")
        ans = 2*args[0]
        for arg in args:
            ans-=arg
        return ans
    except Exception as e:
        print(f"[ERROR] Fail to call minus function:{e} ")
        return None
def mul(*args,**kwargs):
    """
    MUL A*B*C*...
    """
    try:
        print(f"[INFO] mul function is called with args = {args} and kwargs = {kwargs}")
        ans = 1
        for arg in args:
            ans*=arg
        return ans
    except Exception as e:
        print(f"[ERROR] Fail to call mul function:{e} ")
        return None
def div(*args,**kwargs):
    """
    div A/B/C/...
    """
    try:
        print(f"[INFO] div function is called with args = {args} and kwargs = {kwargs}")
        ans = args[0]*ans[0]
        for arg in args:
            ans/=arg
        return ans
    except Exception as e:
        print(f"[ERROR] Fail to call div function:{e} ")
        return None

"""
时间工具函数
"""

def stamp_to_time(stamp:int)->str:
    """
    时间戳->时间
    """
    try:
        print(f"[INFO] stamp_to_time function is called with stamp = {stamp}")
        dateTime = datetime.fromtimestamp(stamp)
        return dateTime.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"[ERROR] Fail to call stamp_to_time function:{e} ")
        return None
    

def time_to_stamp(dateTime:datetime)->int:
    """
    时间->时间戳
    """
    try:
        print(f"[INFO] time_to_stamp function is called with dateTime = {dateTime}")
        return dateTime.timestamp()
    except Exception as e:
        print(f"[ERROR] Fail to call time_to_stamp function:{e} ")
        return None

    
def get_time(*args, **kwargs)->str:
    """
    获取当前时间
    """
    try:
        print(f"[INFO] get_time function is called.")
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"[ERROR] Fail to call get_time function:{e} ")
        return None
    
def get_stamp(*args, **kwargs)->str:
    """
    获取当前时间戳
    """
    try:
        print(f"[INFO] get_stamp function is called.")
        return datetime.now().timestamp()
    except Exception as e:
        print(f"[ERROR] Fail to call get_stamp function:{e} ")
        return None
    
"""
测试与输出函数
"""    

def test(*args, **kwargs):
    """
    TEST
    """
    print(f"[INFO] test function is called with args = {args} and kwargs = {kwargs}")
    return 'the test function has been called'

def creator(*args, **kwargs):
    """
    WHO CREATE THIS RPC?
    """
    print(f"[IMPORTANT]==========================================[IMPORTANT]")
    print(f"[INFO]     MADE BY   **KEFENG DUAN**  ,  **22331016**     [INFO]")
    print(f"[IMPORTANT]==========================================[IMPORTANT]")
    return f"[IMPORTANT] MADE BY KEFENG DUAN, 22331016"


