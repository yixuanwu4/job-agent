def build_digest_html(jobs: list[dict], report_url:str) -> str:
    job_rows = ""
    for i, j in enumerate(jobs):
        bg_color = "#fafafa" if i % 2 == 0 else "#ffffff"
        job_url = j["url"].replace("&", "&amp;")
        job_rows += f"""
        <tr>
        <td style="padding: 16px; background-color: {bg_color}; border-bottom: 1px solid #eee;">
            <a href="{job_url}" style="font-size: 16px; color: #1a1a1a; text-decoration: none; font-weight: 600;">{j['title']}</a>
            <div style="font-size: 13px; color: #666; margin-top: 2px;">{j['company']} · {j['location']}</div>
        </td>
        </tr>
        """

    return f"""
    <div style="background-color: #f4f4f5; padding: 40px 20px;">
        <table style="width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 12px; overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;">
            <tr><td style="padding: 40px 32px 24px;">
                <div style="font-size: 13px; color: #999; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">Daily Job Matches</div>
                <h1 style="font-size: 28px; color: #1a1a1a; margin: 0; font-weight: 700;">{len(jobs)} new opportunities today</h1>
            </td></tr>
            <tr><td style="padding: 0 32px;">
                <table style="width: 100%; border-collapse: collapse;">
                {job_rows}
                </table>
            </td></tr>
            <tr><td style="padding: 32px;">
                <a href="{report_url}" style="display: inline-block; padding: 14px 28px; background: #1a1a1a; color: #fff; text-decoration: none; border-radius: 8px; font-size: 15px; font-weight: 600;">
                View full report →
                </a>
            </td></tr>
        </table>
    </div>
    """