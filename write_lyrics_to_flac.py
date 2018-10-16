import mutagen
import os


def dupfile(pathname):
    '''Detect files with the same filename, ignoring extension.
    Args:
        pathname:The path to be detected.
    Return:
        returns a list of duplicate filenames
    '''
    d = os.path.dirname(pathname)
    ofile = []
    dfile = []
    ext = []
    for dirpath, subpath, files in os.walk(d):
        for file in files:
            if os.path.splitext(file)[0] in ofile:
                dfile.append(os.path.splitext(file)[0])
                ext.append(os.path.basename(file))
            else:
                ofile.append(os.path.splitext(file)[0])
    return dfile


def fileexist(filename, exts):
    '''Check if the file exists.
    Args:
        filename:The filename to be checked.
    Return:
        return filename if it exists.
    '''
    for ext in exts:
        if os.path.exists(filename + ext):
            return filename + ext


def wlyric(dirname, mfiles, exts):
    '''write lyrics to a flac file.
    Args:
        dirname:flac Music file and lyrics file directory,
                music and lyrics have the same file name.
        mfiles:return of function dupfile.
        exts:File suffix name, currently only flac.
    Return:
        return the result of write lyric.
    '''
    for mfile in mfiles:
        try:
            if fileexist(dirname + mfile, exts):
                print(fileexist(dirname + mfile, exts))
                fileinfo = mutagen.File(fileexist(dirname + mfile, exts))
                musiclrc = open(dirname + mfile + ".lrc", "r").read()
                fileinfo['lyrics'] = musiclrc
                fileinfo.save()
                print("歌词写入成功 / The lyrics are successfully written.")
            else:
                print(dirname + mfile + "--------->出错 / Error")
        except Exception as e:
            print(e)


exts = ['.flac']
dirname = "./lyric/"
mfiles = dupfile(dirname)
wlyric(dirname, mfiles, exts)
