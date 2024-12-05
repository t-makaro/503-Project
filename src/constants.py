# for grabbing from SMB file server mapped to L: (LAN ONLY). 
# Otherwise use the 3rd party mirror.
mirror_url = 'L:\\sb-mirror\\' #'https://sb.minibomba.pro/mirror/' 
files = [# 'categoryVotes.csv',
         # 'lockCategories.csv',
         #'ratings.csv',
         'sponsorTimes.csv',
         # 'thumbnailTimestamps.csv',
         # 'thumbnailVotes.csv',
         # 'thumbnails.csv',
         # 'titleVotes.csv',
         # 'titles.csv',
         # 'unlistedVideos.csv',
         'userNames.csv',
         'videoInfo.csv',
         'vipUsers.csv',
         # 'warnings.csv'
        ]

dataset_names = [file.removesuffix('.csv') for file in files]

data_folder = '../data/'

# variables that end with an _ are for processing multiple files into one merged file
unwanted_cols_ = ['Unnamed: 0', 'id', 'hashedVideoID', 'service', 'userAgent']
unwanted_cols = unwanted_cols_ + ['UUID', # unique to every segment
                                  'description', # almost all NaNs
                                  'incorrectVotes', # literally all 1
                                 ]

sb_data_file = data_folder+'merged_data'+'.csv'

#manually specify dtype for columns for import
# sparse_string_dtype = pd.SparseDtype("string")
# sparse_int_dtype = pd.SparseDtype("int")
# sparse_float_dtype = pd.SparseDtype("float")
# sparse_bool_dtype = pd.SparseDtype("bool")

dtypes_ = {
    'category': 'category',
    'actionType': 'category',
    'service': 'category',
    'reason': 'string',
    'videoID': 'string',
    'userID': 'string',
    'votes': 'int',
    'startTime': 'float',
    'endTime': 'float',
    'locked': 'boolean',
    'incorrectVotes': 'int',
    #'timeSubmitted': 'int', # commented due to need to use converter for import
    'view': 'int',
    'videoDuration': 'float',
    'hidden': 'int',
    'reputation': 'float',
    'shadowHidden': 'boolean',
    'userAgent': 'string',
    'description': 'string',
    'remove': 'int',
    'published': 'float', # 'technically int, but it needs to be cast to float later anyway.
}

dtypes = dtypes_ | {'timeSubmitted': 'float'}

# dtypes_sparse = {
#     'reason': sparse_string_dtype,
#     'description': sparse_string_dtype,
#     'hidden': sparse_int_dtype,
#     'votes': sparse_int_dtype,
#     'locked': sparse_int_dtype,
#     'int': sparse_int_dtype,
#     'reputation': sparse_float_dtype,
#     'shadowHidden': sparse_float_dtype,
# }