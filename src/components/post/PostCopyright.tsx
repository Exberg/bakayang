import { author, site } from '@/config.json'
import { getFormattedDateTime } from '@/utils/date'
import { AnimatedSignature } from '../AnimatedSignature'
import { useEffect, useState } from 'react'
import { toast } from "react-toastify";

function getPostUrl(slug: string) {
  return new URL(slug, site.url).href
}

export function PostCopyright({
  title,
  slug,
  lastMod,
}: {
  title: string
  slug: string
  lastMod: Date
}) {
  const [lastModStr, setLastModStr] = useState('')
  const url = getPostUrl(slug)

  function handleCopyUrl() {
    navigator.clipboard.writeText(url)
    toast.success('已复制文章链接')
  }

  useEffect(() => {
    setLastModStr(getFormattedDateTime(lastMod))
  }, [lastMod])

  return (
    <section className="text-xs leading-loose text-secondary">
      <p>Title：{title}</p>
      <p>Author：{author.name}</p>
      <p>
        <span>link：{url}</span>
        <span role="button" className="cursor-pointer select-none" onClick={handleCopyUrl}>
          [copy]
        </span>
      </p>
      <p>last modified：{lastModStr}</p>
      <hr className="my-3 border-primary" />
    </section>
  )
}
