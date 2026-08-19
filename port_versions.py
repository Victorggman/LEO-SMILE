import re

PORT_VERSIONS = {
    20: {
        'service': 'FTP-DATA',
        'probe': b'\n',
        'description': 'File Transfer Protocol (Data)'
    },
    21: {
        'service': 'FTP',
        'probe': b'QUIT\r\n',
        'description': 'File Transfer Protocol'
    },
    22: {
        'service': 'SSH',
        'probe': b'\n',
        'description': 'Secure Shell'
    },
    23: {
        'service': 'TELNET',
        'probe': b'\n',
        'description': 'Telnet Protocol'
    },
    25: {
        'service': 'SMTP',
        'probe': b'HELO test\r\n',
        'description': 'Simple Mail Transfer Protocol'
    },
    53: {
        'service': 'DNS',
        'probe': b'\n',
        'description': 'Domain Name System'
    },
    80: {
        'service': 'HTTP',
        'probe': b'HEAD / HTTP/1.0\r\n\r\n',
        'description': 'Hypertext Transfer Protocol'
    },
    110: {
        'service': 'POP3',
        'probe': b'QUIT\r\n',
        'description': 'Post Office Protocol v3'
    },
    111: {
        'service': 'RPCBIND',
        'probe': b'\n',
        'description': 'Remote Procedure Call'
    },
    135: {
        'service': 'MSRPC',
        'probe': b'\n',
        'description': 'Microsoft RPC'
    },
    139: {
        'service': 'NETBIOS-SSN',
        'probe': b'\n',
        'description': 'NetBIOS Session Service'
    },
    143: {
        'service': 'IMAP',
        'probe': b'CAPABILITY\r\n',
        'description': 'Internet Message Access Protocol'
    },
    443: {
        'service': 'HTTPS',
        'probe': b'HEAD / HTTP/1.0\r\n\r\n',
        'description': 'HTTP over TLS/SSL'
    },
    445: {
        'service': 'SMB',
        'probe': b'\n',
        'description': 'Server Message Block'
    },
    465: {
        'service': 'SMTPS',
        'probe': b'HELO test\r\n',
        'description': 'SMTP over SSL'
    },
    587: {
        'service': 'SMTP',
        'probe': b'HELO test\r\n',
        'description': 'SMTP (Submission)'
    },
    631: {
        'service': 'IPP',
        'probe': b'\n',
        'description': 'Internet Printing Protocol'
    },
    636: {
        'service': 'LDAPS',
        'probe': b'\n',
        'description': 'LDAP over SSL'
    },
    873: {
        'service': 'RSYNC',
        'probe': b'\n',
        'description': 'Rsync File Transfer'
    },
    989: {
        'service': 'FTP-DATA',
        'probe': b'\n',
        'description': 'FTP over SSL (Data)'
    },
    990: {
        'service': 'FTPS',
        'probe': b'\n',
        'description': 'FTP over SSL'
    },
    993: {
        'service': 'IMAPS',
        'probe': b'CAPABILITY\r\n',
        'description': 'IMAP over SSL'
    },
    995: {
        'service': 'POP3S',
        'probe': b'QUIT\r\n',
        'description': 'POP3 over SSL'
    },
    1433: {
        'service': 'MSSQL',
        'probe': b'\x12\x01\x00\x34\x00\x00\x00\x00\x00\x00\x15\x00\x06\x01\x00\x1b\x00\x01\x02\x00\x1c\x00\x0c\x03\x00\x28\x00\x04\xff\x08\x00\x02\x00\x00\x00',
        'description': 'Microsoft SQL Server'
    },
    1521: {
        'service': 'ORACLE',
        'probe': b'\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00',
        'description': 'Oracle Database'
    },
    3306: {
        'service': 'MYSQL',
        'probe': b'\x00\x00\x00\x0a\x35\x2e\x37\x2e\x32\x33\x00\x00\x00',
        'description': 'MySQL Database'
    },
    3389: {
        'service': 'RDP',
        'probe': b'\x03\x00\x00\x13\x0e\x00\x00\x00',
        'description': 'Remote Desktop Protocol'
    },
    5432: {
        'service': 'POSTGRESQL',
        'probe': b'\x00\x00\x00\x08\x04\xd2\x16\x2f',
        'description': 'PostgreSQL Database'
    },
    5900: {
        'service': 'VNC',
        'probe': b'\n',
        'description': 'Virtual Network Computing'
    },
    6379: {
        'service': 'REDIS',
        'probe': b'PING\r\n',
        'description': 'Redis Database'
    },
    8080: {
        'service': 'HTTP-ALT',
        'probe': b'HEAD / HTTP/1.0\r\n\r\n',
        'description': 'HTTP Alternate Port'
    },
    8443: {
        'service': 'HTTPS-ALT',
        'probe': b'HEAD / HTTP/1.0\r\n\r\n',
        'description': 'HTTPS Alternate Port'
    },
    27017: {
        'service': 'MONGODB',
        'probe': b'\x39\x00\x00\x00\x01\x00\x00\x00',
        'description': 'MongoDB Database'
    },
}

VERSION_PATTERNS = {
    'SSH': [
        r'SSH-\d+\.\d+-([^\s]+)',
        r'OpenSSH[_\s]+([\d\.]+)',
        r'sshd[_\s]+([\d\.]+)'
    ],
    'HTTP': [
        r'Server:\s*([^\r\n]+)',
        r'Apache/([\d\.]+)',
        r'nginx/([\d\.]+)',
        r'IIS/([\d\.]+)'
    ],
    'FTP': [
        r'([\w\s]+)\s+\([\d\.]+\)',
        r'vsFTPd\s+([\d\.]+)',
        r'ProFTPD\s+([\d\.]+)'
    ],
    'SMTP': [
        r'([\w\s]+)\s+([\d\.]+)',
        r'Postfix\s+([\d\.]+)',
        r'Exim\s+([\d\.]+)'
    ],
    'MYSQL': [
        r'([\d\.]+)[\s\-]',
        r'MySQL\s+([\d\.]+)',
        r'mariadb\s+([\d\.]+)'
    ],
}

def get_port_info(port):
    return PORT_VERSIONS.get(port, None)

def get_service_name(port):
    info = get_port_info(port)
    return info['service'] if info else 'unknown'

def get_probe(port):
    info = get_port_info(port)
    return info['probe'] if info else b'\n'

def get_description(port):
    info = get_port_info(port)
    return info['description'] if info else 'Unknown Service'

def extract_version(service_type, banner):
    if service_type in VERSION_PATTERNS:
        for pattern in VERSION_PATTERNS[service_type]:
            match = re.search(pattern, banner, re.IGNORECASE)
            if match:
                return match.group(1)
    return None

def is_known_port(port):
    return port in PORT_VERSIONS
