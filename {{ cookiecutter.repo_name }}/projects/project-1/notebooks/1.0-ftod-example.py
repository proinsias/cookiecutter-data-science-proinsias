# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Title
#

# %% [markdown]
# Description with link to ticket.
#

# %%
# %load_ext autoreload
# %autoreload 2
# %matplotlib inline

# %%
import logging
import pathlib

import dotenv
import matplotlib
import matplotlib.pyplot as plt
import nest_asyncio
import numpy as np
import pandas as pd
import seaborn as sns
import ydata_profiling
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display, display_markdown, Markdown
from markupspace import escape
from pqdm.processes import pqdm
# If you want threads instead:
# from pqdm.threads import pqdm
from tqdm.notebook import tqdm

# %%
# pd.options.mode.chained_assignment = None
InteractiveShell.ast_node_interactivity = 'all'
# InteractiveShell.ast_node_interactivity = "last_expr"
tqdm.pandas()

# %%

def printmd(string):
    display(Markdown(escape('# <span style="color:red">'+string+'</span>')))

display_markdown(escape('''## heading
- ordered
- list

The table below:

| id |value|
|:---|----:|
| a  |  1  |
| b  |  2  |
'''), raw=True)

# %% [markdown]
# Blue Alert Box: info.
# <div class="alert alert-block alert-info">
# <b>Tip:</b> Use blue boxes (alert-info) for tips and notes.
# If it's a note, you don't have to include the word "Note".
# </div>
#
# # Yellow Alert Box: Warning.
# <div class="alert alert-block alert-warning">
# <b>Example:</b> Yellow Boxes are generally used to include additional examples or mathematical formulas.
# </div>
#
# # Green Alert Box: Success.
# <div class="alert alert-block alert-success">
# Use green box only when necessary like to display links to related content.
# </div>
#
# # Red Alert Box: Danger.
# <div class="alert alert-block alert-danger">
# It is good to avoid red boxes but can be used to alert users to not delete some important part of code etc.
# </div>

# %%
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
# Add the handler to the logger
logger.addHandler(handler)

matplotlib.use('nbagg')
# prettier plots
plt.style.use('ggplot')
# larger plots - two different ways.
matplotlib.rc('figure', figsize=(15, 10))
plt.rcParams['figure.dpi'] = 90

# larger fonts
sns.set_context('notebook', font_scale=1.5)

dotenv.load_dotenv()
nest_asyncio.apply()

np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)
pd.set_option('display.max_rows', 500)
pd.options.display.max_columns = 50
pd.options.display.max_rows = 100
pd.options.display.max_colwidth = 80
# Adjust the number of columns profiled and displayed by the `info()` method.
pd.options.display.max_info_columns = 150
# Adjust the number of decimals to be displayed in a DataFrame.
pd.options.display.precision = 15
# Adjust the display format in a DataFrame.
# pd.options.display.float_format = '{:.2f}%'.format
# Prints and parses dates with the year first.
pd.options.display.date_yearfirst = True

InteractiveShell.ast_node_interactivity = 'all'

data_dir = pathlib.Path.cwd().parent / 'data'

def square(a):
    return a*a

result = pqdm([1, 2, 3, 4, 5], square, n_jobs=2)

profile = ydata_profiling.ProfileReport(df, title='Profiling Report')
profile.to_notebook_iframe()
# profile.to_widgets()
# profile.to_html('profile.html')
