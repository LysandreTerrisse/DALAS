import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # 브라우저 실행 (headless=True면 창 안 뜸)
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # 유튜브 메인 접속
        await page.goto("https://www.youtube.com/music")
        
        try:
            # 버튼이 있으면 클릭
            reject_btn = await page.wait_for_selector("button:has-text('Reject all')", timeout=5000)
            await reject_btn.click()
            print("쿠키 동의창: 거부 완료")
        except:
            print("쿠키 동의창이 안 떴음 (이미 넘어감)")

        # 로딩 기다리기 (동영상 리스트 뜰 때까지)
        await page.wait_for_selector("a#thumbnail", state="attached")

        # 모든 썸네일 a 태그 가져오기
        elements = await page.query_selector_all("a#thumbnail")

        urls = []
        for el in elements:
            href = await el.get_attribute("href")
            if href and "/watch" in href:
                urls.append("https://www.youtube.com" + href)

        print("수집된 영상 URL:")
        for u in urls:
            print(u)

        await browser.close()

asyncio.run(main())
