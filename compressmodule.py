import zlib,base64

def compress(inputfile,outputfile):
    data=open(inputfile,'r').read()
    data_bytes=bytes(data,'utf-8')
    compress_data=base64.b64encode(zlib.compress(data_bytes,9))
    decoded_data=compress_data.decode('utf-8')
    comp_file=open(outputfile,'w')
    comp_file.write(decoded_data)
def decompress(inputfile,outputfile):
    file_content=open(inputfile,'r').read()
    encode_data=file_content.encode('utf-8')
    decompressed_data=zlib.decompress(base64.b64decode(encode_data))
    decoded_data=decompressed_data.decode('utf-8')
    file=open(outputfile,'w')
    file.write(decoded_data)
    file.close()
compress('demo.txt','ot.txt')
decompress('ot.txt','read.txt')