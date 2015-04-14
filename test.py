from binaryIO import BinaryReader
import struct
import codecs
def export_text(fn):
    dest = codecs.open('entext\\%s.txt'%fn , 'wb' , 'utf-16')
    fp = open(fn , 'rb')
    fStream = BinaryReader(fp)
    count = fStream.ReadInt32()
    for i in xrange(count):
        key = fStream.ReadString().decode('utf-8')
        value = fStream.ReadString().decode('utf-8')
        value = value.replace('\n' , '{0A}\r\n')
        value = value.replace(r'\n' , '{$n}\r\n')
        dest.write('#### %d,%s ####\r\n%s\r\n\r\n'%(i , key , value))
    fp.close()
    dest.close()
export_text('00000000_messages')
    
    
