import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/XUANTIE-RV/openc906"

# Module version
version_str = "0.0.post159"
version_tuple = (0, 0, 159)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post159")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9"
data_version_tuple = (0, 0, 9)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9")
except ImportError:
    pass
data_git_hash = "b0c06eb1f8b3bae663bd8b87eac89ff48e68a57f"
data_git_describe = "v0.0-9-gb0c06eb1f8b3"
data_git_msg = """\
commit b0c06eb1f8b3bae663bd8b87eac89ff48e68a57f
Merge: af5614d72de7 8b1e1bd4556c
Author: Yunhai <shangyunhai@gmail.com>
Date:   Fri Jun 28 20:18:56 2024 +0800

    Merge pull request #16 from xuantiecpu/update_doc
    
    update manuals and datasheet

"""

# Tool version info
tool_version_str = "0.0.post150"
tool_version_tuple = (0, 0, 150)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post150")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_openc906."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_openc906".format(f))
    return fn
