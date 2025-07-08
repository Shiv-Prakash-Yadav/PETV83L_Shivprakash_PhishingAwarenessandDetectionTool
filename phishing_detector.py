def detect_phishing(url):
    suspicious_keywords = ['login', 'verify', 'update', 'bank', 'secure']
    suspicious_domains = ['.tk', '.ml', '.ga', '.cf', '.gq']

    is_suspicious = False
    reason = []

    if any(keyword in url.lower() for keyword in suspicious_keywords):
        is_suspicious = True
        reason.append("Contains suspicious keywords.")

    if any(url.endswith(domain) for domain in suspicious_domains):
        is_suspicious = True
        reason.append("Uses free or uncommon domain.")

    if url.count('.') > 3:
        is_suspicious = True
        reason.append("Too many subdomains.")

    if is_suspicious:
        return f"Phishing Suspected: {'; '.join(reason)}"
    return "Safe URL"