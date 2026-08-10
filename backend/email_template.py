def build_digest_html(jobs: list[dict], report_url:str, manage_url: str) -> str:
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
                See today's best matches →
                </a>
                <p style="font-size: 12px; color: #999; margin-top: 20px; text-align: center;">
                <a href="{manage_url}" style="color: #999;">Update your search or unsubscribe</a>
                </p>
            </td></tr>
        </table>
    </div>
    """

def build_digest_text(jobs: list[dict], report_url:str, manage_url: str) -> str:
    lines = [f"{len(jobs)} new opportunities today\n"]
    for j in jobs:
        lines.append(f"- {j['title']} at {j['company']} ({j['location']})")
        lines.append(f"  {j['url']}\n")
    lines.append(f"\nSee today's best matches: {report_url}")
    lines.append(f"\nUpdate your search or unsubscribe: {manage_url}")
    return "\n".join(lines)

def build_update_link_html(manage_url: str) -> str:
    return f"""
    <div style="background-color: #f4f4f5; padding: 40px 20px;">
        <table style="width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 12px; overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;">
            <tr><td style="padding: 40px 32px;">
                <h1 style="font-size: 22px; color: #1a1a1a; margin: 0 0 16px;">Manage your job search</h1>
                <p style="font-size: 15px; color: #444; line-height: 1.6; margin: 0 0 24px;">
                    Click below to fill in or update your job search details.
                    This link is unique to you — don't share it.
                </p>
                <a href="{manage_url}" style="display: inline-block; padding: 14px 28px; background: #1a1a1a; color: #fff; text-decoration: none; border-radius: 8px; font-size: 15px; font-weight: 600;">
                    Update my information →
                </a>
            </td></tr>
        </table>
    </div>
    """

def build_update_link_text(manage_url: str) -> str:
    return (
        "Manage your job search\n\n"
        "Click the link below to fill in or update your job search details. "
        "This link is unique to you — don't share it.\n\n"
        f"{manage_url}"
    )