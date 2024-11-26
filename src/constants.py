mirror_url = 'https://sb.minibomba.pro/mirror/' #r'E:\docker\sb-mirror\' # for grabbing from SMB file server mapped to E: (LAN ONLY).
mirror_files = [# 'categoryVotes.csv',
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

dataset_names = [file.rstrip('.csv') for file in mirror_files]

data_folder = '../data/'

unwanted_cols = ['Unnamed: 0', 'id', 'hashedVideoID', 'service', 'userAgent']