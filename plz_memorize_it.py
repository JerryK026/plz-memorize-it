import random

# TODO(@seokyung.kim) 2024-10-20
# - [ ] redis 명령어들, 시간복잡도
# - [ ] 암호화 / 보안
# - [ ] mysql update / delete
# - [ ] 정렬 / 트리 / 그래프 종류별
# - [ ] 프로세스 상태
# - [ ] 리눅스 명령어들
# - [ ] 아이노드, 링크
# - [ ] k8s manifest 관리에 필요한 것들
# - [ ] 바이트 등 자료형 단위 등
# - [ ] collation
# - [ ] 리틀 / 빅 엔디안
# - [ ] osi 7계층
# - [ ] cidr 표기법
# - [ ] http 주요 헤더
# - [ ] acid / base
# - [ ] 트랜잭션 격리 수준


knowledge = [
    """
    Latency Comparison Numbers (~2012)
    ----------------------------------
    L1 캐시 참조                                                0.5 ns
    (인스트럭션) 다른 분기 예측                                 5   ns
    L2 캐시 참조                                                7   ns                      14x L1 cache
    뮤텍스 락/언락                                             25   ns
    메인 메모리 참조                                          100   ns                      20x L2 cache, 200x L1 cache
    Zippy로 1K bytes 압축                                   3,000   ns        3 us 
    1 Gbps 네트워크를 통해 1K bytes 전송                   10,000   ns       10 us
    SSD*에서 랜덤으로 4K 읽기                             150,000   ns      150 us          ~1GB/sec SSD
    메모리에서 1MB 순차 읽기                              250,000   ns      250 us
    같은 데이터센터에서 round trip                        500,000   ns      500 us
    SSD*에서 1 MB 순차 읽기                             1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
    디스크 읽기                                        10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
    디스크에서 1MB 순차 읽기                           20,000,000   ns   20,000 us   20 ms  80x memory, 20X SSD
    캘리포니아 -> 네덜란드 -> 캘리포니아 패킷 전송    150,000,000   ns  150,000 us  150 ms
    
    Notes
    -----
    1 ns = 10^-9 seconds
    1 us = 10^-6 seconds = 1,000 ns
    1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns
    
    Credit
    ------
    By Jeff Dean:               http://research.google.com/people/jeff/
    Originally by Peter Norvig: http://norvig.com/21-days.html#answers
    
    Contributions
    -------------
    'Humanized' comparison:    https://gist.github.com/hellerbarde/2843375
    Visual comparison chart:   http://i.imgur.com/k0t1e.png
    Interactive Prezi version: https://prezi.com/pdkvgys-r0y6/latency-numbers-for-programmers-web-development/latency.txt
    
    출처: https://gist.github.com/jboner/2841832
    """,
    """
    http status
    -----
    1xx : 정보 응답
    -----
    2xx : 성공 응답
    -----
    202 Accepted               : 요청 수신하였지만 행동할 수는 없음. 다른 프로세스에서 요청 처리하거나 배치 처리중 (무조건 비동기 응답인 것은 아님)
    204 No Content             : 요청에 대해 보내줄 컨텐츠가 없음. 헤더는 의미 있음.
    -----
    3xx : 리다이렉션 메시지
    -----
    302 Moved Permanently      : 요청한 리소스의 URI가 변경되었음
    304 Not Modified           : 클라이언트에게 응답이 수정되지 않았음을 전달하여 클라이언트는 계속해 응답의 캐시된 버전 사용 가능함
    307 Temporary Redirect     : 클라이언트가 요청한 리소스가 다른 URI에 있으며, 동일한 메소드로 요청해야 함
    -----
    4xx : 클라이언트 에러 응답
    -----
    401 Unauthorized           : 비인증 상태. 로그인 필요함
    403 Forbidden              : 비인가 상태. 콘텐츠에 접근할 권한 없음
    405 Method Not Allowed     : 메소드를 서버에서 알고 있지만 사용할 수는 없음
    409 Conflict               : 요청이 현재 서버 상태와 충돌됨
    415 Unsupported Media Type : 요청한 미디어 포맷은 서버에서 지원하지 않아 서버에서 거절함
    429 Too Many Requests      : 지정된 시간 안에 너무 많은 요청을 보냈음
    -----
    5xx : 서버 에러 응답
    -----
    502 Bad Gateway            : 게이트웨이에서 문제 발생함
    """,
    """
    dns record 종류
    ----------
    A 레코드 : 해당 도메인 주소가 가지는 IP 반환
    CNAME  : 도메인 주소 alias
    AAAA   : IPv6용 A 레코드
    NS     : 네임 서버 권한 관리자 조회. 어떤 도메인에 대한 처리를 다른 도메인 네임 서버에 위임함
    PTR    : IP 주소에 대한 도메인 주소 확인. 1개의 IP당 1개의 도메인 네임 지정 가능
    SOA    : 네임서버가 해당 도메인에 관하여 인증된 데이터를 가지고 있음
    """,
    #TODO(@seokyungkim): 2024-10-20. 시간복잡도 추가해야 함
    """
    redis 명령어 모음 (strings)
    ---------
    key / value 모두 최대 512mb. 알파벳, 한글, 이미지 등 사용 가능.
    - SET  : SET, SETNX, SETEX, SETPEX, MSET, MSETNX, APPEND, SETRANGE
    - GET  : GET, MGET, GETRANGE, STRLEN
    - INCR : INCR, DECR, INCRBY, DECRBY, INCRBYFLOAT
    ---------
    """
]

know = random.choice(knowledge)

print(know)
